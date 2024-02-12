//
// Created by Leonardo Covarrubias on 2/24/23.
//

#include "Echo.h"

using namespace odc::Command;

void Echo::Encode(uint8_t *buffer, uint8_t offset = 0) {
    buffer[offset] = state_;
}

uint32_t Echo::GetEncodingSize() {
    return encodingSize;
}
