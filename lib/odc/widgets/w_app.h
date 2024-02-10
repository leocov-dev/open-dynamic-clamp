//
// Created by Leonardo Covarrubias on 8/15/23.
//

#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_W_APP_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_W_APP_H

#include "w_status_bar.h"

namespace odc {
    namespace Widgets {
        class WApp {

        public:
            explicit WApp();

            void Draw();


        private:
            WStatusBar w_status_bar;
        };
    }
}


#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_W_APP_H
