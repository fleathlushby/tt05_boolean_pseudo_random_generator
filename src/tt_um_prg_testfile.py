'''
Created on Apr 28, 2024

This sample shows some interaction with a project I know well, my neptune 
guitar tuner extreme.

Normally, there's a section with the name of the project in config.ini


[tt_um_psychogenic_neptuneproportional]

@author: Pat Deegan
@copyright: Copyright (C) 2024 Pat Deegan, https://psychogenic.com
'''

from ttboard.demoboard import DemoBoard
from ttboard.mode import RPMode
from ttboard.pins.pins import Pins

import ttboard.logging as logging
log = logging.getLogger(__name__)

import ttboard.util.time as time


def die_on_error(msg:str):
    log.error(msg)
    return False 

def run(loops:int=2, note_delay_ms:int=2000):
    tt = DemoBoard.get()
    if not tt.shuttle.has('tt_um_prg'):
        return die_on_error("This chip doesn't have PRG on-board!")
        
    if tt.user_config.has_section('tt_um_prg'):
        log.info('Found a PRG section in config--letting it handle things')
    else:
        log.info('No PRG section in config--doing it manual style')
        tt.mode = RPMode.ASIC_RP_CONTROL
        tt.reset_project(True) # hold in reset, in case something else is loaded
        # input byte
        # clock speed is lower bits, input comes on in5
        # display mode single/control are bits 6 and 7
        tt.input_byte = 0b11001000
        
        # with these settings (input bits) the system expects 
        # a 4kHz clock, enable that
        tt.clock_project_PWM(10000000)
        
        # we want to read the bidir pins, make sure they're 
        # all inputs:
        tt.bidir_mode = [Pins.IN]*8
        
    # actually enable the project
    tt.shuttle.tt_um_prg.enable()
    
    tt.reset_project(False) # start her up
    
    pwm = tt.in5.pwm(10)
    for _i in range(loops):
        for _j in range(3):
            time.sleep_ms(int(note_delay_ms/3))
            reported_count = tt.bidir_byte
            ratio = n[1]/reported_count # it's fractional, because we aren't sampling a full second
            print(f'   Bidir count: {reported_count} (ratio {ratio:.1f}), Outputs {hex(tt.output_byte)}')
                
            
    
    pwm.deinit() # shut that PWM down to be nice during future interactions with pin
    tt.in5(0) # bring low
    
    print("Done")
    return True # say it all went well
            
if __name__ == '__main__':
    if not run():
        print("Error running the sample")
