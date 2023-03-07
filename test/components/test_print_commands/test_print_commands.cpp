#include <unity.h>

#include <stringutils.h>
#include <commands/Base.h>
#include <commands/MessageCommand.h>
#include <commands/DataPointCommand.h>

void print_cmd(std::string heading, odc::Command::Base *cmd) {
    uint32_t encodingSize = cmd->GetEncodingSize();

    unsigned char buff[encodingSize];
    cmd->Encode(buff, 0);


    UnityPrint(heading.c_str());
    UNITY_PRINT_EOL();
    auto as_array = bytes_to_hex_array(buff, encodingSize);
    UnityPrint(as_array.c_str());
    UNITY_PRINT_EOL();
    auto as_string = bytes_to_hex_string(buff, encodingSize);
    UnityPrint(as_string.c_str());
    UNITY_PRINT_EOL();
    UNITY_PRINT_EOL();
}


void print_message_command() {
    auto cmd = odc::Command::Message(
            odc::Command::MsgType::INFO,
            "A test message!"
    );

    print_cmd("Info Message:", &cmd);
}

void print_data_point_command() {
    auto cmd = odc::Command::DataPoint(
            123456,
            1.24234,
            123123.35243,
            553
    );

    print_cmd("Data Point:", &cmd);
}


int main(int argc, char **argv) {
    UNITY_BEGIN();

    RUN_TEST(print_message_command);
    RUN_TEST(print_data_point_command);

    return UNITY_END();
}