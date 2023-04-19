#pragma once

#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>


typedef struct Token {
    enum Type {
        OPERATOR,
        ID,
    };

    char* string;
    uint32_t line;
    uint32_t column;
} Token_T;

std::vector<Token_T> tokenize_file (char* file_path);
