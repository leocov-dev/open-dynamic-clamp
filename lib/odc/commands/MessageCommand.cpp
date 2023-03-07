//
// Created by Leonardo Covarrubias on 2/24/23.
//

#include "MessageCommand.h"


using namespace odc::Command;

void Message::Encode(unsigned char *buff, uint8_t offset) {
    buff[offset] = kind_;
    offset += 1;
    memcpy(&buff[offset], &len_, SizeInt);
    offset += SizeInt;
    memcpy(&buff[offset], msg_, len_);
}

uint32_t Message::GetEncodingSize() {
    return encodingSize;
}
