![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg)

# Boolean function based pseudo random generator
Design of a Boolean function based pseudo random generator for submission to the Tiny Tapeout-05 run.

<!-- [pseudorandomgenerator](https://github.com/fleathlushby/tt05_boolean_pseudo_random_generator/assets/105290202/82b0348a-03e5-4525-b8eb-a1f6d74e7db5 "Schematic of the Boolean function based pseudo random generator") -->  
**Principle of operation of Boolean function based pseudo random generator** 
This implementation of a pseudo random generator contains linear mappings to and from the following blocks:
- one $GF(2^4)$ normal base
- three instances of $GF(2^4)$ multipliers
- one $GF(2^4)$ inverter and
- one square scaler.  
The input and output strings of the pseudo random generator are split into five and three shares, respectively. This pseudo random generator generates random values based on these five input parameters or variables. Instead of relying solely on a single seed or input, it takes several inputs thereby introducing more control over the randomness of the generated values. Thus, the multiple input bytes are used as seeds. These five random input bytes are generated externally from a randomness source. For example, factors like time, user-provided data, environmental conditions, and previous random values can be considered to produce a sequence of random numbers that are influenced by a combination of these inputs. This can result in a more tailored or context-aware randomness, which can be valuable in various applications such as simulations, games, cryptography, or data generation. The operation of the Boolean function based pseudo random generator can be classified into the following three phases.

**First phase- Affine transformation**  
In the first phase, three shares are processed by the linear input mapping and afterwards fed into a multiplier and a uniform reduction to two shares $(a,b,c)\mapsto(a,b \oplus c)$ is fed into the square scaler. 
The output of the multiplier is partially remasked by 8 bits of randomness while the square scaler output is left as is. We use fresh randomness at the end of the first phase to satisfy uniformity during the combination of the square scaler’s and the multiplier’s outputs. The result is saved in a register. 

**Second phase- Finite field inversion**  
In the second phase, the overall five shares are combined into four shares. Due to the previous remasking, this can be done uniformly as such:
      
$$(x,y,a,b,c)\mapsto(x,y \oplus (r_1 \oplus r_2),a \oplus (b \oplus r_1),c \oplus r_2)$$

In the above equation, $x,y$ denote the square scaler output, while $a,b,c$ denote the multiplier output. Note that a register needs to hold all five shares before recombination to prevent leakage. After recombination, the four shares are fed into the inverter and remasked with 8 bits of randomness. A register stage, preventing glitches, follows this inverter. 

**Third phase- Finite field multiplication and inverse linear mapping**  
In the final stage, the remasked outputs are reduced to three shares uniformly by the following function.
      
$$(a,b,c,d)\mapsto(a \oplus (b \oplus r_3),c \oplus r_4,d \oplus r_3 \oplus r_4)$$
      
Subsequently, these shares are fed into two multipliers. Finally, the inverse linear mapping follows. With this construction, it is enough to have three input shares to the generator since the multiplier block requires only three shares. At this stage, we again add a randomness after the inverter to break the dependency between the inputs of the multipliers in the third phase.  
In general, we need to reduce the number of shares from five to four at the end of the first phase as the inverter in the second phase can process four input strings. Moreover, the multipliers in the final stage is capable of processing three shares of input thus enforcing the reduction of shares from four to three at the end of the second phase.
