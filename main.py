#from parse import *

types = [
    "u32",
    "i32",
    "nul",
    "str",
    "chr"
]

file = open("test.a");
file_contents = file.read();
file_contents_formatted = file_contents.replace('\n', ' ');
file_lines_array = file_contents.splitlines();

# Array of tuples defining the start and end index of function definitions
#[ (start_indx, end_indx), ]
function_definitions = [];
string_locations = [];

function_index = 0;
in_function_def = False;
string_index = 0;
in_string = False;

def string_checks(char):
    if char == "'" or char == '"':
        if in_string:
            string_index += 1;
            string_locations[string_index][0] = char_index;
        elif not in_string:
            string_locations[string_index][1] = char_index;
        in_string = not in_string;
    
    if in_string:
        char_index += 1;
        return True;
    return False;

operation = 0;
char_index = 0;
for char in file_contents_formatted:
    if string_checks(char):
        continue;

    
    if char == ' ':
        # operation += 1;
        char_index += 1;
        continue;



    if char 
    char_index += 1;
