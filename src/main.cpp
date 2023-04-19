#include <string>
#include <vector>

#include "ALPHA/lexer.hpp"

int main(int argc, char* argv[]) {
    std::cout << argv[0] << '\n';
    std::cout << argv[1] << '\n';
    if (argc < 2) {
        std::cout << "No target file specified...\n";
        return 1;
    }
    
    std::vector<Token_T> tokens = tokenize_file(argv[1]);

    return 0;
}
