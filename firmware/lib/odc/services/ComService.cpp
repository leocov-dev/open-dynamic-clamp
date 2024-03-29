//
// Created by Leonardo Covarrubias on 2/11/23.
//

#include "ComService.h"
#include "commands/Echo.h"


void odc::Services::ComService::SendCommand(odc::Command::Base &cmd) {
    uint8_t offset = 1;
    const size_t buffSize = offset + cmd.GetEncodingSize();
    unsigned char buff[buffSize];
    buff[0] = cmd.GetType();
    cmd.Encode(buff, offset);

    send_(buff, buffSize);
}
