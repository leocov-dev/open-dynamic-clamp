//
// Created by Leonardo Covarrubias on 8/15/23.
//

#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_W_STATUS_BAR_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_W_STATUS_BAR_H

#include "w_connection.h"

namespace odc {
    namespace Widgets {
        class WStatusBar {
        public:
            explicit WStatusBar() {
                w_connection = WConnection();
            }

            void Draw();

        private:
            WConnection w_connection;
        };
    }
}

#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_W_STATUS_BAR_H
