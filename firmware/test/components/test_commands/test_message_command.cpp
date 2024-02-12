#include <unity.h>

#include <utils/stringutils.h>
#include <commands/Message.h>

void test_message_command() {
    auto cmd = odc::Command::Message(
            odc::Command::MsgType::INFO,
            "A test message!"
    );

    uint32_t encodingSize = cmd.GetEncodingSize();

    unsigned char buff[encodingSize];
    cmd.Encode(buff, 0);

    auto formatted = odc::utils::bytes_to_hex_string(buff, encodingSize);

    UnityPrint(formatted.c_str());
    UNITY_PRINT_EOL();

    unsigned char expected[] = {0x02, 0x0f, 0x00, 0x00, 0x00, 0x41, 0x20, 0x74, 0x65, 0x73, 0x74, 0x20, 0x6d, 0x65,
                                0x73, 0x73, 0x61, 0x67, 0x65, 0x21};

    TEST_ASSERT_EQUAL_CHAR_ARRAY(expected, buff, encodingSize);
}


int main(int argc, char **argv) {
    UNITY_BEGIN();

    RUN_TEST(test_message_command);

    return UNITY_END();
}