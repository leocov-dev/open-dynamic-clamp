//
// Created by Leonardo Covarrubias on 3/6/23.
//
#include <sstream>
#include <iomanip>
#include "stringutils.h"


std::string odc::utils::byte_to_hex_string_elem(unsigned char b) {
    std::stringstream stream;
    stream << R"(\x)"
           << std::setfill('0')
           << std::setw(2)
           << std::hex
           << (unsigned int) b;
    return stream.str();
}

std::string odc::utils::bytes_to_hex_string(unsigned char *b, size_t size) {
    std::stringstream stream;
    stream << "\"";
    for (unsigned int i = 0; i < size; i++) {
        stream << odc::utils::byte_to_hex_string_elem(b[i]);
    }
    stream << "\"";

    return stream.str();
}

std::string odc::utils::bytes_to_hex_array(unsigned char *b, size_t size) {
    std::stringstream stream;
    for (unsigned int i = 0; i < size; i++) {
        if (i == 0) {
            stream << "{" << odc::utils::byte_to_hex_array_elem(b[i]);
        } else {
            stream << ", " << odc::utils::byte_to_hex_array_elem(b[i]);
        }
    }
    stream << "}";

    return stream.str();
}

std::string odc::utils::byte_to_hex_array_elem(unsigned char b) {
    std::stringstream stream;
    stream << R"(0x)"
           << std::setfill('0')
           << std::setw(2)
           << std::hex
           << (unsigned int) b;

    return stream.str();
}

