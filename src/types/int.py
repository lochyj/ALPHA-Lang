import src.values as values

def check_length(split_line: list[str], line: str):
    if len(split_line) != 4:
        print(f"Interpreter error at: {line}, Length of input for int type smaller or larger than expected.");
        exit();

def output_ref_check(val: str, line: str):
    if val.startswith('$'):
        if val[1] != '-':
            print(f"Interpreter error at: {line}, Unexpected character after stack reference.");
            exit();
        elif values.output_index < int(val[2]):
            print(f"Interpreter error at: {line}, Reference to stack is out of bounds. Negative index for return array.");
            exit();
        return True;
    else:
        return False

def handle_replace(line: str):
    split_line = line.split(' ');
    input1 = 0;
    input2 = 0;

    val1 = split_line[1]
    val2 = split_line[3]

    if output_ref_check(val1, line):
        input1 = values.output[values.output_index - int(val1[2])];
    
    if output_ref_check(val2, line):
        input2 = values.output[values.output_index - int(val2[2])];
    
    if val1 in values.const:
        input1 = values.const[val1];
    
    if val2 in values.const:
        input2 = values.const[val2];

    if not val1.startswith('$') and val1 not in values.const:
        input1 = int(val1);
    
    if not val2.startswith('$') and val2 not in values.const:
        input2 = int(val2);

    return [input1, input2];


def parse_line_int(line: str):
    split_line = line.split(' ');

    check_length(split_line, line);
    
    replaced_vals = handle_replace(line);

    input1 = replaced_vals[0];
    input2 = replaced_vals[1];
    
    operand = split_line[2];
    match operand:
        # Start basic operators
        case '+':
            values.output[values.output_index] = input1 + input2;
        case '-':
            values.output[values.output_index] = input1 - input2;
        case '/':
            values.output[values.output_index] = input1 / input2;
        case '*':
            values.output[values.output_index] = input1 * input2;
        case '&':
            values.output[values.output_index] = input1 & input2;
        case '%':
            values.output[values.output_index] = input1 % input2;
        case '|':
            values.output[values.output_index] = input1 | input2;
        case '^':
            values.output[values.output_index] = input1 ** input2;
        case "==":
            values.output[values.output_index] = input1 == input2;
        case "!=":
            values.output[values.output_index] = input1 != input2;
        case '<':
            values.output[values.output_index] = input1 < input2;
        case '>':
            values.output[values.output_index] = input1 > input2;
        case ">=":
            values.output[values.output_index] = input1 >= input2;
        case "<=":
            values.output[values.output_index] = input1 <= input2;
        #End basic operators

        #TODO: Implement more advanced operators
        
        case _:
            print(f"Interpreter error at: {line}, Unknown operator.");
            exit();
    
    values.output_index += 1;
