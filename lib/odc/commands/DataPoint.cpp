//
// Created by Leonardo Covarrubias on 3/4/23.
//

#include "DataPoint.h"

using namespace odc::Command;

void DataPoint::Encode(uint8_t *buffer, uint8_t offset = 0) {
    memcpy(&buffer[offset], &timestamp_, SizeLong);
    offset += SizeLong;
    memcpy(&buffer[offset], &membrane_, SizeFloat);
    offset += SizeFloat;
    memcpy(&buffer[offset], &inject_, SizeFloat);
    offset += SizeFloat;
    memcpy(&buffer[offset], &cycle_, SizeFloat);
}

uint32_t DataPoint::GetEncodingSize() {
    return encodingSize;
}
