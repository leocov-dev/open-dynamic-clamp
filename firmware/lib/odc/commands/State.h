//
// Created by Leonardo Covarrubias on 5/23/23.
//

#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_STATE_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_STATE_H

#include "Base.h"

namespace odc::Command {

    enum StateType : uint8_t {
        PING = 1,
        PONG = 2,
    };

    enum StateResource : uint8_t {
        CONNECTION = 1,
        CALIBRATION_DATA = 2,
    };


    class State : public Base {

    public:
        explicit State(const StateType type, const StateResource resource) :
                Base(Type::STATE),
                type_(type),
                resource_(resource) {};

    private:
        StateType type_;
        StateResource resource_;
        const uint32_t encodingSize = SizeInt * 2;
    };
}


#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_STATE_H
