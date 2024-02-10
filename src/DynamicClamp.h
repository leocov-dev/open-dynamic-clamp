//
// Created by Leonardo Covarrubias on 2/11/23.
//

#ifndef DY_CLAMP_DYNAMIC_CLAMP_H
#define DY_CLAMP_DYNAMIC_CLAMP_H

#include <iostream>

#include "services/ComService.h"
#include "display/SpiPins.h"
#include "display/DisplayService.h"
#include "commands/Message.h"
#include "commands/DataPoint.h"
#include "commands/Echo.h"



namespace odc {

    template<class DisplayDriver>
    class DynamicClamp {
    public:
        DynamicClamp(Services::ComService *cs, Display::DisplayService<DisplayDriver> *ds)
                : display_(ds),
                  comsService_(cs) {};

        void Tick();

        void HandleCommand(Command::Base *cmd) {
            std::cout << "handle: " << cmd << std::endl;
        }


    private:
        odc::Display::DisplayService<DisplayDriver> *display_;
        odc::Services::ComService *comsService_;
    };

    template<class DisplayDriver>
    void DynamicClamp<DisplayDriver>::Tick() {
        display_->Clear();
        display_->SplashScreen();
        std::cout << "tick" << std::endl;
        display_->Show();
        std::cerr << "tock" << std::endl;
    }
}
#endif //DY_CLAMP_DYNAMIC_CLAMP_H
