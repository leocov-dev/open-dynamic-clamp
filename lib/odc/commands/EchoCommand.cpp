//
// Created by Leonardo Covarrubias on 2/24/23.
//

#include "EchoCommand.h"

using namespace odc::Command;

void Echo::Encode(uint8_t *buff, uint8_t offset) {
    buff[offset] = state_;
}

uint32_t Echo::GetEncodingSize() {
    return encodingSize;
}
