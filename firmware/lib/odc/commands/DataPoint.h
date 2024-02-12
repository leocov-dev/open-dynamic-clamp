//
// Created by Leonardo Covarrubias on 3/4/23.
//

#ifndef ODC_FIRMWARE_DATAPOINTCOMMAND_H
#define ODC_FIRMWARE_DATAPOINTCOMMAND_H

#include <cstring>
#include "Base.h"

namespace odc::Command {

    class DataPoint : public Base {
    public:
        explicit DataPoint(
                const uint64_t timestamp,
                const float membrane,
                const float inject,
                const float cycle
        ) :
                Base(Type::DATA_POINT),
                timestamp_(timestamp),
                membrane_(membrane),
                inject_(inject),
                cycle_(cycle) {}

        void Encode(unsigned char *buffer, uint8_t offset) override;

        uint32_t GetEncodingSize() override;

    private:
        const uint64_t timestamp_;
        const float membrane_;
        const float inject_;
        const float cycle_;

        const uint32_t encodingSize = SizeLong + (3 * SizeFloat);
    };


}

#endif //ODC_FIRMWARE_DATAPOINTCOMMAND_H
