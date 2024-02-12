//
// Created by Leonardo Covarrubias on 8/15/23.
//

#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_W_CONNECTION_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_W_CONNECTION_H

namespace odc {
    namespace Widgets {
        class WConnection {
        public:
            void setConnected(bool value);

            void Draw();
        };
    }
}

#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_W_CONNECTION_H
