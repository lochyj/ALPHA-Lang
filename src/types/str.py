import src.values as values

def return_string(string: str):
    # Removes the last character from the string. This means that we remove the unwanted whitespace at the trailing end of the string.
    if string.endswith(" "):
        string = string[:-1];
    values.output[values.output_index] = string;

def parse_line_str(line: str):
    split_line = line.split(' ');

    if not len(split_line) > 1:
        print(f"Interpreter error at: {line}, No input string specified for type string.");
        exit();
    
    temp: str = "";
    i = 0;
    while i < len(split_line) - 1:
        temp += split_line[i+1] + ' ';
        i += 1;
    
    return_string(temp);

    values.output_index += 1;