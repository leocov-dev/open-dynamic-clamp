//
// Created by Leonardo Covarrubias on 3/4/23.
//

#include "DataPointCommand.h"

using namespace odc::Command;

void DataPoint::Encode(uint8_t *buff, uint8_t offset) {
    memcpy(&buff[offset], &timestamp_, SizeLong);
    offset += SizeLong;
    memcpy(&buff[offset], &membrane_, SizeFloat);
    offset += SizeFloat;
    memcpy(&buff[offset], &inject_, SizeFloat);
    offset += SizeFloat;
    memcpy(&buff[offset], &cycle_, SizeFloat);
}

uint32_t DataPoint::GetEncodingSize() {
    return encodingSize;
}
