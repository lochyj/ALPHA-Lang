#include <stdio.h>
#include <stdlib.h>

enum op {
    ADD,    // Add
    SUB,    // Subtract
    MOV,    // Move / create var
    RLP,    // Run loop until var is equal to supplied value
    ELP     // End loop
};

typedef struct {

} op_line_t;

int main(int argc, char** argv) {
    // get file from argv
    FILE* file = fopen(argv[1], "rb");
    if( !file ) {
        perror(argv[1]);
        exit(1);
    }

    fseek(file , (long) 0, SEEK_END);
    long fsize = ftell(file);
    rewind(file);

    char* buffer;

    buffer = calloc(1, fsize + 1);
    if (!buffer) {
        fclose(file);
        fputs("memory alloc failed", stderr);
        exit(1);
    }

    /* copy the file into the buffer */
    if( 1 != fread(buffer, fsize, 1 , file)) {
        fclose(file);
        free(buffer);
        fputs("entire read fails", stderr);
        exit(1);
    }

    fclose(file);

    // run main
    printf("%s\n", buffer);

    free(buffer);
    return 0;
}