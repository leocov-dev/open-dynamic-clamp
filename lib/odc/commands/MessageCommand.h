//
// Created by Leonardo Covarrubias on 2/24/23.
//

#ifndef ODC_FIRMWARE_MESSAGECOMMAND_H
#define ODC_FIRMWARE_MESSAGECOMMAND_H

#include <cstring>
#include <cstdint>
#include "Base.h"

namespace odc::Command {

    enum MsgType : uint8_t {
        DEBUG = 1,
        INFO = 2,
        WARN = 3,
        ERROR = 4,
    };

    class Message : public Base {
    public:
        explicit Message(const MsgType kind, const char *msg) :
                Base(Type::MSG),
                kind_(kind),
                msg_(msg),
                len_(strlen(msg)),
                encodingSize(SizeByte + SizeInt + len_) {};

        void Encode(uint8_t *buff, uint8_t offset) override;
        uint32_t GetEncodingSize() override;

    private:
        MsgType kind_;
        const char *msg_;
        uint32_t len_;
        const uint32_t encodingSize;
    };

} // odc

#endif //ODC_FIRMWARE_MESSAGECOMMAND_H
