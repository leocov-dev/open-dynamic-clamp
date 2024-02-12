//
// Created by Leonardo Covarrubias on 2/11/23.
//



#ifndef DY_CLAMP_COMMUNICATION_H
#define DY_CLAMP_COMMUNICATION_H


#include <utility>
#include <functional>
#include "commands/Base.h"
#include "commands/Echo.h"

namespace odc::Services {

    class ComService {
    public:

        typedef std::function<void(const uint8_t *buffer, size_t size)> SendFunc;

        explicit ComService(SendFunc func) : send_(std::move(func)) {};

        ~ComService() = default;

        void SendCommand(odc::Command::Base &cmd);

        template<typename Cmd>
        Cmd decode(const uint8_t *buffer, size_t size) {
            return odc::Command::Echo(true);
        }

    private:
        SendFunc send_;

    };

}  // end namespace odc

#endif //DY_CLAMP_COMMUNICATION_H
