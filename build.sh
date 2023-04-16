clang++ -I ./include/ -c src/main.cpp -o build/main.o
clang++ -I ./include/ -c src/lexer.cpp -o build/lexer.o

g++ -o ./build/main.out ./build/main.o ./build/lexer.o

./build/main.out
