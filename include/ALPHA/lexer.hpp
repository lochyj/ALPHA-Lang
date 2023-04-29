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
#include <algorithm>

#define RED  "\x1B[31m"

enum TYPE {
    WORD,
    DELINEATOR,
    STRING,
    INT,
};

typedef struct Token {
    int id;
    TYPE type;
    std::string symbol;
    uint32_t line;
    uint32_t column;
} Token_T;

std::vector<Token_T> tokenize_file (char* file_path);

static bool is_delineator(char character);
