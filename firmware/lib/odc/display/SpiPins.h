//
// Created by Leonardo Covarrubias on 2/25/23.
//

#include <cinttypes>

#ifndef ODC_FIRMWARE_SPI_H
#define ODC_FIRMWARE_SPI_H

namespace odc {
    namespace Display {
        struct SpiPins {
            // HARDWARE SPI CLK, MOSI
            const int8_t DC;
            const int8_t CS;
            const int8_t RESET;
        };
    }
}

#endif //ODC_FIRMWARE_SPI_H
