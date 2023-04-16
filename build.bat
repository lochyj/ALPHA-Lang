clang++ -I ./include/ -c src/main.cpp -o build/main.o
clang++ -I ./include/ -c src/lexer.cpp -o build/lexer.o

clang-cl /out:build/main.exe ./build/main.o ./build/lexer.o