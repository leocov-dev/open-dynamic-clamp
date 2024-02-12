//
// Created by Leonardo Covarrubias on 5/23/23.
//

#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_UTILS_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_UTILS_H

#include <cstdint>
#include <cstring>
#include "Base.h"
#include "Echo.h"

namespace odc::Command {

    template <typename Cmd>
    Cmd decode(const uint8_t *buffer, size_t size) {

        return odc::Command::Echo(true);
    }

}


#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_UTILS_H
