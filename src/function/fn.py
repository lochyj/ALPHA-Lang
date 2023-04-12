import src.values as values

def parse_line_fncall(line: str):
    split_line = line.split(' ');
    val = 0;
    
    if split_line[2].startswith('$'):
        if split_line[2][1] != '-':
            print(f"Interpreter error at: {line}, Unexpected character after stack reference.");
            exit();
        else:
            if values.output_index < int(split_line[2][2]):
                print(f"Interpreter error at: {line}, Reference to stack is out of bounds. Negative index for return array.");
                exit();
            else:
                val = values.output[values.output_index - int(split_line[2][2])];
    
    if split_line[2] in values.const:
        val = values.const[split_line[2]];

    if not split_line[2].startswith('$'):
        if split_line[2] not in values.const:
            val = split_line[2];

    if split_line[1] not in values.fn_types:
        if split_line[1] in values.fn_builtins:
            tmp = values.fn_builtins[split_line[1]](val);
            if tmp != None:
                values.output[values.output_index] = tmp;
                tmp = None;
                values.output_index += 1;
        elif split_line[1] in values.fn_user:
            tmp = values.fn_user[split_line[1]](val);
            if tmp != None:
                values.output[values.output_index] = tmp;
                tmp = None;
                values.output_index += 1;
        else:
            print(f"Interpreter error at: {line}, Unknown function call; Function neither builtin nor user defined.");
            exit();
    else:
        print(f"Interpreter error at: {line}, Missing function call or definition.");
        exit();
    values.output_index += 1;