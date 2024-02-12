import enum


class CalParam(enum.IntEnum):
    AMP_i = 1
    AMP_o = 2
    ADC_m = 3
    ADC_n = 4
    DAC_m = 5
    VLT_d = 6


class CndctParam(enum.IntEnum):
    G_Shunt = 1
    G_H = 2
    G_Na = 3
    OU1_m = 4
    OU1_D = 5
    OU2_m = 6
    OU2_D = 7
    G_EPSC = 8
