g++ -I ./include/ -c src/main.cpp -o build/main.o
g++ -I ./include/ -c src/lexer.cpp -o build/lexer.o

g++ -o ./build/main.bin ./build/main.o ./build/lexer.o

./build/main.bin /home/lochyj/Documents/GitHub/ALPHA-Lang/test.al
