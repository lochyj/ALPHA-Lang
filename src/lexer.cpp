#include <iostream>
#include <fstream>
#include <cstdbool>

#include "lexer.hpp"

// From https://github.com/Electrux/Ethereal/blob/master/src/FE/Lexer.cpp
#define CURRENT( line ) ( line[ i ] )
#define NEXT( line ) ( i + 1 < ( int )line.size() ? line[ i + 1 ] : 0 )
#define PREVIOUS( line ) ( line.size() > 0 && i - 1 >= 0 ? line[ i - 1 ] : 0 )


int TokenizeFile(char* file_dir) {
    // std::ifstream file;
    // file.open(file_dir, std::ios::in);
    // std::string data;
    // file >> data;
    return 0;
}

// int a = 10; int b = 20;
int TokenizeLine(std::string line, int line_num, int line_len) {
    bool in_comment = false;
    for (int i = 0; i < line_len; i++) {
        printf("%c\n", CURRENT(line));
        if (isspace(CURRENT(line)))
            continue;

        if (CURRENT(line) == '*' && NEXT(line) == '/') {
            i++;
            in_comment = false;
            continue;
        }
        
        if (in_comment)
            continue;

        if (CURRENT(line) == '/' && NEXT(line) == '/') {
            return 0;
        }

        if (CURRENT(line) == '/' && NEXT(line) == '*') {
            in_comment = true;
            continue;
        }
    }
    return 0;
}