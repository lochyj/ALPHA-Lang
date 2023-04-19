#include "ALPHA/lexer.hpp"

#define CURRENT(line) (line[i])
#define NEXT(line) (i + 1 < (int)line.size() ? line[i + 1] : 0)
#define PREVIOUS(line) (line.size() > 0 && i - 1 >= 0 ? line[i - 1] : 0)

std::vector<Token_T> tokenize_file (char* file_path) {
    std::vector<Token_T> tokens;

    std::ifstream file(file_path);

    if (!file.is_open()) {
        std::cout << "ERROR Cannot open: " << file_path << '\n';
    }

    std::stringstream buffer;
    buffer << file.rdbuf();

    std::string code = buffer.str();

    bool in_comment = false;
    bool in_string = false;


    for (int i = 0; i < code.length(); i++) {

        if (CURRENT(code) == '*' && NEXT(code) == '/') {
            in_comment = false;
            i++;
            continue;
        }

        if (in_comment)
            continue;

        if (CURRENT(code) == '/' && NEXT(code) == '*') {
            in_comment = true;
            i++;
            continue;
        }



        std::cout << CURRENT(code) << std::endl;

    }

    return tokens;
}

char* operators[3] {
    "int",
    "string",
    "char",
}

bool is_operator_char(char op_char) {
    return false;
}
