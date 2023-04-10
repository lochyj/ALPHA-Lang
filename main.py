from parse import *

file = open("test.a");
file_contents = file.read();
file_lines_array = file_contents.splitlines()

for i in file_lines_array:
    parse_line(i);
