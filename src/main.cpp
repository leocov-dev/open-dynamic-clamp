
#include <iostream>
#include <sstream>
#include <SPI.h>
#include <Arduino.h>
#include <PacketSerial.h>
#include <DynamicClamp.h>

#include "version.h"
#include "commands/utils.h"
#include "services/ComService.h"

PacketSerial packetSerial;
odc::Services::ComService *comService;


#include <Adafruit_SH110X.h>

const odc::Display::SpiPins pins = {
        6,
        5,
        10
};
Adafruit_SH1106G *displayDriver;
odc::Display::DisplayService<Adafruit_SH1106G> *displayService;
odc::DynamicClamp<Adafruit_SH1106G> *app;


extern "C" {
std::stringstream stream;

[[maybe_unused]] int _write(int fd, const char *ptr, int len) {
    (void) fd;
    auto type = odc::Command::MsgType::DEBUG;
    if (fd == 2) {
        type = odc::Command::MsgType::ERROR;
    }


    int count = len;
    while (count--) {
        stream << *ptr++;
    }

    auto msg = odc::Command::Message(type, stream.str().c_str());
    comService->SendCommand(msg);
    stream.str("");
    stream.clear();
    return len;
}
}

void setup() {

    comService = new odc::Services::ComService(
            [](const uint8_t *buffer, size_t size) {
                packetSerial.send(buffer, size);
            });

    displayDriver = new Adafruit_SH1106G(128, 64, &SPI, pins.DC, pins.RESET, pins.CS);
    displayService = new odc::Display::DisplayService<Adafruit_SH1106G>(displayDriver, ODC_VERSION);

    app = new odc::DynamicClamp<Adafruit_SH1106G>(comService, displayService);

    packetSerial.begin(115200);
    packetSerial.setPacketHandler([](const uint8_t *buffer, size_t size) {
        auto cmd = comService->decode<odc::Command::Echo>(buffer, size);

    });

    std::cout << "setup done" << std::endl;
}


void loop() {
    packetSerial.update();

    app->Tick();

    delay(500);
}