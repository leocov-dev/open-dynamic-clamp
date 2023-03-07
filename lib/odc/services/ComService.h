//
// Created by Leonardo Covarrubias on 2/11/23.
//


#include <functional>
#include <utility>
#include "commands/Base.h"

#ifndef DY_CLAMP_COMMUNICATION_H
#define DY_CLAMP_COMMUNICATION_H


namespace odc::Services {

    class ComService {
    public:

        typedef std::function<void(const uint8_t* buffer, size_t size)> SendFunc;


        explicit ComService(SendFunc func): send_(std::move(func)) {};
        ~ComService() = default;

        void SendCommand(odc::Command::Base &cmd);

        void HandleCommand(const uint8_t* buffer, size_t size);

    private:
        SendFunc send_;

    };

}  // end namespace odc

#endif //DY_CLAMP_COMMUNICATION_H
