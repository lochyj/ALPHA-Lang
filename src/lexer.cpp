#include "ALPHA/lexer.hpp"

#define CURRENT(line) ((char)(line[i]))
#define NEXT(line) ((char)(i + 1 < (int)line.size() ? line[i + 1] : 0))
#define NEXT2(line) ((char)(i + 2 < (int)line.size() ? line[i + 2] : 0))
#define PREVIOUS(line) ((char)(line.size() > 0 && i - 1 >= 0 ? line[i - 1] : 0))

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
    std::string string_segment;
    int id = 0;

    for (int i = 0; i < code.length(); i++) {
        std::cout << "E: ";

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
        
        if (!in_string) {
            if (CURRENT(code) == '"') {
                in_string = true;
                std::cout << CURRENT(code) << '\n';
                continue;
            }
        }

        if (in_string) {
            if (CURRENT(code) == '"') {
                std::cout << "A: ";

                tokens[id].symbol = string_segment;
                tokens[id].id = id;
                tokens[id].type = TYPE::STRING;
                tokens[id].column = 10;
                tokens[id].line = 10;
                id++;
                std::cout << string_segment << '\n';
                string_segment = '\0';
                in_string = false;
                continue;
            } else {
                string_segment.push_back(CURRENT(code));
            }
            std::cout << CURRENT(code) << '\n';
            continue;
        }

        if (is_delineator(CURRENT(code))) {
            tokens[id].symbol.push_back(CURRENT(code));
            tokens[id].id = id;
            tokens[id].type = TYPE::DELINEATOR;
            tokens[id].column = 10;
            tokens[id].line = 10;
            id++;

            std::cout << "Delineator: " << CURRENT(code) << '\n';

            continue;
        }

        std::cout << CURRENT(code) << '\n';

    }

    return tokens;
}


// These characters delineate words such as: <word> & <word> where "&" is a delineator.
// Its function isn't necessary in this context and will be determined later.
std::vector<char> delineators = {
    ';',
    '(',
    ')',
    '{',
    '}',
    '[',
    ']',
    '.',
    '=',
    '*',
    '^',
    '&',
    '-',
    '+',
    '@',
    '#',
    '$',
    '%',
    '~',
    '"',
    '\'',
    '\\',
    '|',
    '<',
    '>',
};

static bool is_delineator(char character) {
    std::cout << "\nIs Delin: " << character;
    if (std::find(delineators.cbegin(), delineators.cend(), character) != delineators.cend()) {
        std::cout << "True\n";
        return true;
    }
    std::cout << "False\n";
    return false;
}
