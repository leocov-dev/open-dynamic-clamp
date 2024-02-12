import pytest

from modules.commands import ParamCommand, ParamMapType
from modules.commands.enum.command_enums import CommandType
from modules.commands.enum.param_enums import CalParam


def test_calibration_command_encode_decode():
    param_map: ParamMapType = {
        CalParam.AMP_i: 1.234,
        CalParam.AMP_o: 3.456,
        CalParam.ADC_m: 100,
        CalParam.ADC_n: 2345.243,
        CalParam.DAC_m: 32.452345,
        CalParam.VLT_d: 40000,
    }

    cc = ParamCommand(CommandType.CAL_PARAM, param_map)

    encoded = cc.encode()

    decoded: ParamCommand = ParamCommand.decode(CommandType.CAL_PARAM, encoded)

    for k, v in param_map.items():
        assert pytest.approx(decoded[k]) == v
