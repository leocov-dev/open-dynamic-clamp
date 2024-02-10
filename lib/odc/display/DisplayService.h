//
// Created by Leonardo Covarrubias on 2/25/23.
//

#include <string>
#include <utility>
#include "Bitmap.h"
#include "widgets/w_app.h"


#ifndef ODC_FIRMWARE_DISPLAYSERVICE_H
#define ODC_FIRMWARE_DISPLAYSERVICE_H


namespace odc {
    namespace Display {
        template<class DisplayDriver>
        class DisplayService {

        public:
            explicit DisplayService(DisplayDriver *driver, std::string version)
                    : version_(std::move(version)), oled_(driver) {
                w_app = odc::Widgets::WApp();

                oled_->begin();
                oled_->clearDisplay();
                DrawGraphBounds();
                WaitingForSerial();
                oled_->display();
            };

            void SplashScreen();

            void Clear();

            void Show();

            template<uint8_t w, uint8_t h, uint16_t s>
            void DrawBitmap(uint8_t x, uint8_t y, const Bitmap <w, h, s> *bitmap);

            void DrawGraphBounds();

            void WaitingForSerial();

        private:

            std::string version_;
            DisplayDriver *oled_;
            odc::Widgets::WApp w_app;
        };

        template<class D>
        void DisplayService<D>::SplashScreen() {
            DrawBitmap(0, 0, &open_dynamic_clamp_splash);
            oled_->setTextSize(1);
            oled_->setTextColor(0);
            oled_->setCursor(1, 1);
            oled_->write(version_.c_str());
            oled_->setTextColor(1);
        }

        template<class D>
        void DisplayService<D>::DrawGraphBounds() {

            oled_->drawRect(0, 0, 128, 64, 1);

            oled_->drawRect(1, 15, 62, 48, 1);
            oled_->drawRect(65, 15, 62, 48, 1);
        }

        template<class D>
        template<uint8_t w, uint8_t h, uint16_t s>
        void DisplayService<D>::DrawBitmap(uint8_t x, uint8_t y, const Bitmap <w, h, s> *bitmap) {
            oled_->drawBitmap(x, y, bitmap->data, bitmap->width, bitmap->height, 1);
        }

        template<class D>
        void DisplayService<D>::Clear() {
            oled_->clearDisplay();
        }

        template<class D>
        void DisplayService<D>::Show() {
            oled_->display();
        }

        template<class D>
        void DisplayService<D>::WaitingForSerial() {
            DrawBitmap(90, 3, &conn_off);
            DrawBitmap(112, 3, &conn_on);

            oled_->setCursor(2, 16);
            oled_->setTextColor(1);
            oled_->print("Waiting\nfor\nconnection...");
        }

    }
}


#endif //ODC_FIRMWARE_DISPLAYSERVICE_H
