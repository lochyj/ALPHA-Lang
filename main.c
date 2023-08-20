#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

enum {
    ADD,    // Add
    SUB,    // Subtract
    MOV,    // Move / create var
    RLP,    // Run loop until var is equal to supplied value
    ELP,    // End loop
    INC,    // Increment var
    DEC,    // Decrement var
    FINISH
};

int add(int x, int y) {
    return x + y;
}

int sub(int x, int y) {
    return x - y;
}

int mov(int x, int y) {
    return x;
}

int rlp(int x, int y) {
    return x;
}

void elp(void) {
    ;
}

void inc(int* x) {
    *x += 1;
}

void dec(int* x) {
    *x -= 1;
}

char* operators[FINISH] = {
    "add",
    "sub",
    "mov",
    "rlp",
    "elp",
    "inc",
    "dec"
};

uintptr_t* operators_functions[FINISH] = {
    (uintptr_t*) &add,
    (uintptr_t*) &sub,
    (uintptr_t*) &mov,
    (uintptr_t*) &rlp,
    (uintptr_t*) &elp,
    (uintptr_t*) &inc,
    (uintptr_t*) &dec
};

void parse_line(char* line, int len) {

    // If line is empty
    if (len < 3) {
        return;
    }

    // Its probably a comment
    if (line[0] == ';') {
        return;
    }

    // All operators are of length 3
    char* operator = calloc(1, sizeof(char) * 3);

    // check if operator is valid
    for (int i = 0; i < FINISH; i++) {
        if (line[0] == operators[i][0] && line[1] == operators[i][1] && line[2] == operators[i][2]) {
            operator = operators[i];
            break;
        }
    }

    // get operands
    char* operands = calloc(1, sizeof(char) * (len - 3));
    for (int i = 0; i < len - 3; i++) {
        operands[i] = line[i + 4];
    }

    printf("%s : %s", operator, operands);

}

int main(int argc, char** argv) {
    // get file from argv
    FILE* file = fopen(argv[1], "rb");
    size_t length;
    size_t read;
    char* line = NULL;

    if(!file) {
        perror(argv[1]);
        exit(1);
    }

    fclose(file);

    while ((read = getline(&line, &length, file)) != -1) {
        parse_line(line, read);
    }

    return 0;
}