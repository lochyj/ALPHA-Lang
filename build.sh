g++ -I ./include/ -c src/main.cpp -o build/main.o
g++ -I ./include/ -c src/lexer.cpp -o build/lexer.o

g++ -o ./build/main.out ./build/lexer.o ./build/main.o

./build/main.out /home/lochyj/Documents/GitHub/ALPHA-Lang/test.al
