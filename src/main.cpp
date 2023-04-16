#include <cstdio>
#include <vector>
#include <string>

#include "lexer.hpp"

int main(int argc, char* argv[]) {
    // TEMP
    char* input_file = argv[1];

    std::string line = "int a = 10;";

    TokenizeLine(line, 1, line.size());
}