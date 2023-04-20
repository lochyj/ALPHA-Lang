#include "ALPHA/lexer.hpp"

#define CURRENT(line) (line[i])
#define NEXT(line) (i + 1 < (int)line.size() ? line[i + 1] : 0)
#define NEXT2(line) (i + 2 < (int)line.size() ? line[i + 2] : 0)
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
    std::string string_segment;
    int id = 0;

    int operator_index = 0;
    bool is_operator = false;
    std::string operator_str;

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

        if (CURRENT(code) == '"') {
            in_string = !in_string;
        } else if (CURRENT(code) == '\'') {
            if (NEXT2(code) != '\'') {
                printf("Error: Unexpected character at end of char definition: %c%c%c <- Here\n", CURRENT(code), NEXT(code), NEXT2(code));
                printf("                                                         ^\n");
                printf("Suggested: Replace with \"'\"\n");
                break;
            }
        }

        if (in_string) {
            if (CURRENT(code) == ' ') {
                tokens[id].symbol = string_segment;
                tokens[id].id = id;
                tokens[id].type = TYPE::STR;
                tokens[id].column = 10;
                tokens[id].line = 10;
                id++;
                string_segment = "";
                continue;
            }
            string_segment += CURRENT(code);
            continue;
        }

        if (is_operator_char(CURRENT(code), operator_index)) {
            std::cout << "Operator char: " << CURRENT(code) << std::endl;
            operator_str += CURRENT(code);
            operator_index++;
            is_operator = true;

            if (!is_operator_char(NEXT(code), operator_index)) {
                if (is_operator_str(operator_str)) {
                    std::cout << "Operator: " << operator_str << std::endl;
                    tokens[id].type = TYPE::OP;
                    tokens[id].symbol = operator_str;
                    tokens[id].line = 10;    // 10 is temp
                    tokens[id].column = 10;  // 10 is temp
                    tokens[id].id = id;
                    id++;
                    std::cout << "Added operator";
                }
            }

            continue;
        } else if (operator_index > 0) {
            operator_index = 0;
            operator_str = "";
            is_operator = false;
        }



        std::cout << CURRENT(code) << std::endl;

    }

    return tokens;
}

// TODO: make this an array of vectors. maybe...

const std::string operators[7] = {
    "int",
    "string",
    "char",
    "for",
    "struct",
    "while",
    "do",
};

int operators_len = 7;

bool is_operator_char(char op_char, int op_index) {
    for (int i = 0; i < operators_len; i++) {
        if (operators[i][op_index] == op_char) {
            return true;
        }
    }
    return false;
}

bool is_operator_str(std::string str) {
    for (int i = 0; i < operators_len; i++) {
        if (operators[i].compare(str)) {
            return true;
        }
    }
    return false;
}
