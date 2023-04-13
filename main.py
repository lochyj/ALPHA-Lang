from src.values import *
from src.parse import *

file = open("test.a");
file_contents = file.read();
file_lines_array = file_contents.splitlines();


for line in file_lines_array:
    parse_line(line);
    continue;

print(f"Output array: {output}");
