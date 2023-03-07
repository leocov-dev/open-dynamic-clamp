//
// Created by Leonardo Covarrubias on 2/25/23.
//

#include "Bitmap.h"


#ifndef ODC_FIRMWARE_DISPLAYSERVICE_H
#define ODC_FIRMWARE_DISPLAYSERVICE_H


namespace odc::Display {
    template<class DisplayDriver>
    class DisplayService {
    public:
        explicit DisplayService(DisplayDriver *driver)
                : oled_(driver) {
            oled_->begin();
            SetMustClear();
        };

        void SplashScreen();

        void Clear();

        void Show();

        void SetMustClear();

        template<uint8_t w, uint8_t h, uint16_t s>
        void DrawBitmap(uint8_t x, uint8_t y, const Bitmap<w, h, s> *bitmap);

        void DrawGraphBounds();

        void WaitingForSerial();

    private:


        DisplayDriver *oled_;
        bool must_clear_ = false;
    };

    template<class D>
    void odc::Display::DisplayService<D>::SplashScreen() {
        DrawBitmap(0, 0, &open_dynamic_clamp_splash);
        oled_->setTextSize(1);
        oled_->setTextColor(0);
        oled_->setCursor(1, 1);
//    oled_->write(ODC_VERSION);
        oled_->setTextColor(1);
    }

    template<class D>
    void odc::Display::DisplayService<D>::DrawGraphBounds() {

        oled_->drawRect(0, 0, 128, 64, 1);

        oled_->drawRect(1, 15, 62, 48, 1);
        oled_->drawRect(65, 15, 62, 48, 1);
    }

    template<class D>
    void odc::Display::DisplayService<D>::SetMustClear() {
        must_clear_ = true;
    }

    template<class D>
    template<uint8_t w, uint8_t h, uint16_t s>
    void odc::Display::DisplayService<D>::DrawBitmap(uint8_t x, uint8_t y, const Bitmap<w, h, s> *bitmap) {
        oled_->drawBitmap(x, y, bitmap->data, bitmap->width, bitmap->height, 1);
    }

    template<class D>
    void odc::Display::DisplayService<D>::Clear() {
        if (must_clear_) {
            oled_->clearDisplay();
            must_clear_ = false;
        }
    }

    template<class D>
    void odc::Display::DisplayService<D>::Show() {
        oled_->display();
    }

    template<class D>
    void odc::Display::DisplayService<D>::WaitingForSerial() {
        oled_->setCursor(2, 16);
        oled_->setTextColor(1);
        oled_->print("Waiting for connection...");
    }

}


#endif //ODC_FIRMWARE_DISPLAYSERVICE_H
