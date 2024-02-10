//
// Created by Leonardo Covarrubias on 3/6/23.
//


#ifndef OPEN_DYNAMIC_CLAMP_FIRMWARE_STRINGUTILS_H
#define OPEN_DYNAMIC_CLAMP_FIRMWARE_STRINGUTILS_H

#include <string>

namespace odc::utils {

    std::string bytes_to_hex_string(unsigned char *b, size_t size);

    std::string byte_to_hex_string_elem(unsigned char b);

    std::string bytes_to_hex_array(unsigned char *b, size_t size);

    std::string byte_to_hex_array_elem(unsigned char b);
}


#endif //OPEN_DYNAMIC_CLAMP_FIRMWARE_STRINGUTILS_H
