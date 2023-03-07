//
// Created by Leonardo Covarrubias on 2/24/23.
//

#include <cstdint>
#include "Base.h"

#ifndef ODC_FIRMWARE_ECHOCOMMAND_H
#define ODC_FIRMWARE_ECHOCOMMAND_H

namespace odc::Command {
    class Echo : public Base {
    public:
        explicit Echo(const bool state) :
                Base(Type::ECHO),
                state_(state) {};

        void Encode(uint8_t *buff, uint8_t offset) override;

        uint32_t GetEncodingSize() override;

    private:
        bool state_;
        const uint32_t encodingSize = 1;
    };
}


#endif //ODC_FIRMWARE_ECHOCOMMAND_H
