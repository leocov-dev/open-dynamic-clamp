//
// Created by Leonardo Covarrubias on 2/11/23.
//

#ifndef DY_CLAMP_COMMAND_H
#define DY_CLAMP_COMMAND_H

#include <cstdint>

namespace odc::Command {
    enum Type : unsigned char {
        ECHO = 1,               // rw <->
        MSG = 2,                // wo  ->
        CALIBRATION_PARAM = 3,  // rw <->
        CONDUCTANCE_PARAM = 4,  // rw <->
        DATA_POINT = 5,         // wo  ->
    };

    class Base {
    public:
        virtual ~Base() = default;

        virtual void Encode(unsigned char *buff, uint8_t offset) = 0;

        virtual uint32_t GetEncodingSize() = 0;

        Type GetType();

    protected:
        explicit Base(const Type type) : type(type) {};
        const Type type;
        static const uint8_t SizeByte = 1;
        static const uint8_t SizeShort = 2;
        static const uint8_t SizeInt = 4;
        static const uint8_t SizeFloat = 4;
        static const uint8_t SizeLong = 8;

    };
}
#endif //DY_CLAMP_COMMAND_H
