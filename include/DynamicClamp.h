//
// Created by Leonardo Covarrubias on 2/11/23.
//

#include <Arduino.h>
#include "services/ComService.h"
#include "display/SpiPins.h"
#include "display/DisplayService.h"
#include "commands/MessageCommand.h"
#include "commands/DataPointCommand.h"
#include "commands/EchoCommand.h"

#ifndef DY_CLAMP_DYNAMIC_CLAMP_H
#define DY_CLAMP_DYNAMIC_CLAMP_H


namespace odc {

    template <class Driver>
    class DynamicClamp {
    public:
        DynamicClamp(Services::ComService *cs, Display::DisplayService<Driver> *ds)
                : display_(ds),
                  comsService_(cs) {};

        void Tick();

    private:
        odc::Display::DisplayService<Driver> *display_;
        odc::Services::ComService *comsService_;
    };

    template <class D>
    void DynamicClamp<D>::Tick() {
//    comsService_->CheckIfSerialReady();

        display_->Clear();
//    if (!comsService_->Connected()) {
//        display_->SplashScreen();
//        display_->Show();
//        display_->SetMustClear();
//    } else {
        display_->DrawGraphBounds();
        display_->Show();

        // TODO: delay between blocks while testing messaging
        //  decrease to evaluate message decode speed of workbench app
        uint16_t tick = 50;

// ------------------------------------------------------------------------------
        Command::Echo echoOn = Command::Echo(true);
        comsService_->SendCommand(echoOn);
        delay(tick);
        Command::Echo echoOff = Command::Echo(false);
        comsService_->SendCommand(echoOff);
        delay(tick);

// ------------------------------------------------------------------------------
        Command::Message debug = Command::Message(Command::MsgType::DEBUG,
                                                  "don't need to be seeing this!");
        comsService_->SendCommand(debug);
        delay(tick);
        Command::Message info = Command::Message(Command::MsgType::INFO, "hi there from micro");
        comsService_->SendCommand(info);
        delay(tick);
        Command::Message warn = Command::Message(Command::MsgType::WARN, "uh oh this is a warning...");
        comsService_->SendCommand(warn);
        delay(tick);
        Command::Message err = Command::Message(Command::MsgType::ERROR,
                                                "ACK! something really bad happened!!!");
        comsService_->SendCommand(err);
        delay(tick);

// ------------------------------------------------------------------------------
        Command::DataPoint data_p = Command::DataPoint(
                12345,
                3.435,
                30.99888,
                0.03
        );
        comsService_->SendCommand(data_p);
        delay(tick);

        Command::DataPoint data_p_2 = Command::DataPoint(
                3402938432,
                3.435,
                30.99888,
                0.03
        );
        comsService_->SendCommand(data_p_2);
        delay(tick);


//    }
    }
}
#endif //DY_CLAMP_DYNAMIC_CLAMP_H
