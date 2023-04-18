#include "ALPHA/lexer.hpp"

#define CURRENT(line) (line[i])
#define NEXT(line) (i + 1 < (int)line.size() ? line[i + 1] : 0)
#define PREVIOUS(line) (line.size() > 0 && i - 1 >= 0 ? line[i - 1] : 0)

std::vector<Token_T> tokenize_file (char* file_path) {
    std::vector<Token_T> tokens;

    std::cout << "Called... " << file_path << '\n';

    std::ifstream file(file_path);

    if (!file.is_open())
        std::cout << "ERROR Cannot open: " << file_path << '\n';

    std::string code;

    if(file) {
      std::ostringstream ss;
      ss << file.rdbuf(); // reading data
      code = ss.str();
    }

    std::cout << code;

    bool in_comment = false;
    bool in_string = false;
    int i = 0;

    while (!file.eof()) {
        i++;
        if (CURRENT(code) == ' ') {
            continue;
        }

        if (CURRENT(code) == '*' && CURRENT(code) == '/') {
            in_comment = false;
            continue;
        }

        if (in_comment)
            continue;

        if (CURRENT(code) == '/' && CURRENT(code) == '*') {
            in_comment = true;
            continue;
        }
    }

    return tokens;
}
