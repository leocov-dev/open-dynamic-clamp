#include <Arduino.h>
#include <SPI.h>
#include <Adafruit_SH110X.h>
#include <PacketSerial.h>
#include <DynamicClamp.h>

const odc::Display::SpiPins pins = {
        6,
        5,
        10
};

PacketSerial packetSerial;
Adafruit_SH1106G displayDriver = Adafruit_SH1106G(128, 64, &SPI, pins.DC, pins.RESET, pins.CS);

odc::Services::ComService *comService;
odc::Display::DisplayService<Adafruit_SH1106G> *displayService;

odc::DynamicClamp<Adafruit_SH1106G> *app;


void setup() {
    packetSerial.begin(115200);
    comService = new odc::Services::ComService(
            [](const uint8_t *buffer, size_t size) {
                packetSerial.send(buffer, size);
            });
    packetSerial.setPacketHandler([](const uint8_t* buffer, size_t size){
        comService->HandleCommand(buffer, size);
    });

    displayService = new odc::Display::DisplayService<Adafruit_SH1106G>(&displayDriver);

    app = new odc::DynamicClamp(comService, displayService);
}

void loop() {
    app->Tick();
    packetSerial.update();
}