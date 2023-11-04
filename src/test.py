import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

input1 = [0x62, 0x04, 0x05, 0xf8, 0x95]
output1 = [0x0, 0x0, 0x55, 0xa2, 0x0c]
input2 = [0x9b, 0x04, 0x05, 0xf8, 0x95]
output2 = [0x0, 0x0, 0x4c, 0x5d, 0xa9]
input3 = [0x77, 0x04, 0x05, 0xf8, 0x95]
output3 = [0x0, 0x0, 0xce, 0xf2, 0x04]

@cocotb.test()
async def test_prg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    dut._log.info("reset")
    #Input set 1
    dut.rst_n.value = 0
    dut.ena.value = 0
    await ClockCycles(dut.clk, 6)
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.ui_in.value = input1[0]
    # dut._log.info("output at reset low = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input1[1]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input1[2]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input1[3]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input1[4]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ena.value = 0
    await ClockCycles(dut.clk, 3)
    dut._log.info("output after input buffering = {}".format(int(dut.uo_out.value)))
    dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    assert dut.uio_oe == 0xFF
    assert dut.uio_out == 0x01
    for i in range(5):
        assert int(dut.uo_out.value) == output1[i]
        await ClockCycles(dut.clk, 1)
    #Input set 2
    await ClockCycles(dut.clk, 6)
    dut.rst_n.value = 0
    dut.ena.value = 0
    await ClockCycles(dut.clk, 6)
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.ui_in.value = input2[0]
    # dut._log.info("output at reset low = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input2[1]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input2[2]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input2[3]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input2[4]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ena.value = 0
    await ClockCycles(dut.clk, 3)
    dut._log.info("output after input buffering = {}".format(int(dut.uo_out.value)))
    dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    assert dut.uio_oe == 0xFF
    assert dut.uio_out == 0x01
    for i in range(5):
        assert int(dut.uo_out.value) == output2[i]
        await ClockCycles(dut.clk, 1)
    #Input set 3
    await ClockCycles(dut.clk, 6)
    dut.rst_n.value = 0
    dut.ena.value = 0
    await ClockCycles(dut.clk, 6)
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.ui_in.value = input3[0]
    # dut._log.info("output at reset low = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input3[1]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input3[2]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input3[3]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input3[4]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ena.value = 0
    await ClockCycles(dut.clk, 3)
    dut._log.info("output after input buffering = {}".format(int(dut.uo_out.value)))
    dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    assert dut.uio_oe == 0xFF
    assert dut.uio_out == 0x01
    for i in range(5):
        assert int(dut.uo_out.value) == output3[i]
        await ClockCycles(dut.clk, 1)
