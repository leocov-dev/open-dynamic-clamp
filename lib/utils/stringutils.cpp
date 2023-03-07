//
// Created by Leonardo Covarrubias on 3/6/23.
//
#include <sstream>
#include <iomanip>
#include "stringutils.h"

std::string byte_to_hex_string_elem(unsigned char b) {
    std::stringstream stream;
    stream << R"(\x)"
           << std::setfill('0')
           << std::setw(2)
           << std::hex
           << (int) b;
    return stream.str();
}

std::string bytes_to_hex_string(unsigned char *b, size_t size) {
    std::stringstream stream;
    stream << "\"";
    for (int i = 0; i < size; i++) {
        stream << byte_to_hex_string_elem(b[i]);
    }
    stream << "\"";

    return stream.str();
}

std::string bytes_to_hex_array(unsigned char *b, size_t size) {
    std::stringstream stream;
    for (int i = 0; i < size; i++) {
        if (i == 0) {
            stream << "{" << byte_to_hex_array_elem(b[i]);
        } else {
            stream << ", " << byte_to_hex_array_elem(b[i]);
        }
    }
    stream << "}";

    return stream.str();
}

std::string byte_to_hex_array_elem(unsigned char b) {
    std::stringstream stream;
    stream << R"(0x)"
           << std::setfill('0')
           << std::setw(2)
           << std::hex
           << (int) b;

    return stream.str();
}

