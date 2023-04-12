import src.values as values

def check_length(line: str):
    split_line = line.split(' ');

    if len(split_line) > 2:
        print(f"Interpreter error at: {line}, Char type input is longer than expected.");
        exit();

    elif len(split_line[1]) > 1:
        print(f"Interpreter error at: {line}, Char type input is not a char it is a string.");
        exit();

def parse_line_char(line: str):
    split_line = line.split(' ');
    
    check_length(line);

    values.output[values.output_index] = split_line[1];
    values.output_index += 1;

