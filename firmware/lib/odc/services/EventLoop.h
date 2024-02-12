//
// Created by Leonardo Covarrubias on 5/24/23.
//

#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_EVENTLOOP_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_EVENTLOOP_H

#include <queue>
#include <functional>
#include "commands/Base.h"

namespace odc::Services {

    enum EventType {
        CONNECTED = 1,
        DISCONNECTED = 2,
        ECHO = 3,
    };

    class Event {
    public:
        explicit Event(EventType type, odc::Command::Base *cmd) : cmd_(cmd), type_(type) {};

        ~Event() = default;

        EventType GetType() {
            return type_;
        };

        odc::Command::Base *GetCommand() {
            return cmd_;
        }

    private:
        odc::Command::Base *cmd_;
        EventType type_;
    };

    class EventLoop {
    public:

        typedef std::function<void(Event event)> HandlerFunc;

        ~EventLoop() = default;

        void AddEvent(Event event) {
            queue_.push(event);
        }

        void ProcessEvents() {
            while (!queue_.empty()) {
                auto event = queue_.front();

                for (const HandlerFunc& h: handlers_) {
                    h(event);
                }

                queue_.pop();
            }
        }

    private:
        std::vector<HandlerFunc> handlers_;
        std::queue<Event> queue_;
    };
}


#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_EVENTLOOP_H
