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

#define RED  "\x1B[31m"

enum TYPE {
    WORD,
    OPERATOR,
    STRING
};

typedef struct Token {
    int id;
    TYPE type;
    std::string symbol;
    uint32_t line;
    uint32_t column;
} Token_T;

std::vector<Token_T> tokenize_file (char* file_path);

bool is_operator_char(char op_char, int op_index);
bool is_operator_str(std::string str);
