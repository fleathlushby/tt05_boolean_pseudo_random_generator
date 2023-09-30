import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

input = [0x62, 0x04, 0x05, 0xf8, 0x95]
output = [0x0, 0x0, 0x55, 0xa2, 0x0c]

@cocotb.test()
async def test_prg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    dut._log.info("reset")
    dut.rst_n.value = 0
    dut.ena.value = 0
    await ClockCycles(dut.clk, 6)
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.ui_in.value = input[0]
    # dut._log.info("output at reset low = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input[1]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input[2]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input[3]
    # dut._log.info("output during input buffering = {}".format(int(dut.uo_out.value)))
    # dut._log.info("output ready = {}".format(int(dut.uio_out.value)))
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = input[4]
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
        assert int(dut.uo_out.value) == output[i]
        await ClockCycles(dut.clk, 1)
