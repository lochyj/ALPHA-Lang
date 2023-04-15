import src.values as values
from src.variables import define_variable
from src.evaluate import call_function

def line_defines_var(line: list[str]):
    if line[0] in values.types.keys():
        return True;
    else:
        return False;

def line_defines_fn(line: str):
    if line[0] == values.fn_type and line[1] in values.types.keys():
        return True;
    else:
        return False;

def parse_mid_file(file):
    lines = file.split('\n');

    split_lines = [];

    for line in lines:
        split_lines.append(line.split(' '))

    skip_number = 0;
    for line in split_lines:
        if skip_number > 0:
            skip_number -= 1;
            continue;
        
        if line_defines_var(line):
            define_variable(line);
        elif line_defines_fn(line):
            ...
            # Get all of the lines that are within that function

        if line[0] in values.functions.keys():
            call_function(line);
        
