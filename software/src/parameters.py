from modules.commands.enum.command_enums import CommandType
from modules.commands.enum.param_enums import (
    CalParam,
    CndctParam,
)
from modules.widgets.param_list_widget import ParamConfig, ParamData

PARAMETERS: ParamConfig = {
    "Conductance": {
        "type": CommandType.COND_PARAM,
        "icon": ":/app/icons/conductance",
        "data": {
            CndctParam.G_Shunt: ParamData("G_Shunt", 2.0, min_val=0, max_val=100, step=1, unit="nS"),
            CndctParam.G_H: ParamData("G_H", 0.0, min_val=0, max_val=100, step=1, unit="nS"),
            CndctParam.G_Na: ParamData("G_Na", 0.0, min_val=0, max_val=100, step=1, unit="nS"),
            CndctParam.OU1_m: ParamData("OU1_m", 0.0, min_val=100, max_val=0, step=1, unit="nS"),
            CndctParam.OU1_D: ParamData("OU1_D", 0.0, min_val=0, max_val=100, step=1, unit="nS²/mS"),
            CndctParam.OU2_m: ParamData("OU2_m", 0.0, min_val=100, max_val=0, step=1, unit="nS"),
            CndctParam.OU2_D: ParamData("OU2_D", 0.0, min_val=0, max_val=100, step=1, unit="nS²/mS"),
            CndctParam.G_EPSC: ParamData("G_EPSC", 0.0, min_val=0, max_val=100, step=1, unit="nS"),
        },
    },
    # leave calibration at bottom
    "Calibration": {
        "type": CommandType.CAL_PARAM,
        "icon": ":/app/icons/calibration",
        "data": {
            CalParam.AMP_i: ParamData("AMP_i", 50.0, min_val=0, max_val=1000, step=10, unit="mV/mV"),
            CalParam.AMP_o: ParamData("AMP_o", 400.0, min_val=0, max_val=1000, step=10, unit="pA/V"),
            CalParam.ADC_m: ParamData("ADC_m", 5.5, min_val=0, max_val=100, step=10, unit="mV/1"),
            CalParam.ADC_n: ParamData("ADC_n", -11500.0, min_val=-20000, max_val=0, step=100, unit="mV"),
            CalParam.DAC_m: ParamData("DAC_m", 50, min_val=0, max_val=100, step=1, unit="%"),
            CalParam.VLT_d: ParamData("VLT_d", 0.0, min_val=0, max_val=1000, step=10, unit="mV"),
        },
    },
    # add more above calibration
}
