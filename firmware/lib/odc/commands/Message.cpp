//
// Created by Leonardo Covarrubias on 2/24/23.
//

#include "Message.h"


using namespace odc::Command;

void Message::Encode(unsigned char *buffer, uint8_t offset = 0) {
    buffer[offset] = kind_;
    offset += 1;
    memcpy(&buffer[offset], &len_, SizeInt);
    offset += SizeInt;
    memcpy(&buffer[offset], msg_, len_);
}

uint32_t Message::GetEncodingSize() {
    return encodingSize;
}
