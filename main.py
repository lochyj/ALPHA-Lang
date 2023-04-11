file = open("test.a");
file_contents = file.read();
file_lines_array = file_contents.splitlines();

types = [
    "int",
    "char",
    "str",
    "null",
    "fn",
    "//"
];

const = {
    "PI": 3.1415926
}

output = {};
output_index = 0;

for line in file_lines_array:
    if line == '':
        continue;

    line_return_type = "null";
    val1 = None;
    val2 = None;
    operand = None;

    broken_line = line.split(' ');
    
    if broken_line[0] not in types:
        print(f"Interpreter error at: {line}, Missing type definition.");
        exit();
    else:
        line_return_type = broken_line[0];
    
    if line_return_type == "//":
        # Continue because it's a comment.
        continue;

    if line_return_type == "int":
        if len(broken_line) < 4 or len(broken_line) > 4:
            print(f"Interpreter error at: {line}, Length of input smaller or larger than expected.");
            break;
        val1 = 0;
        val2 = 0;
        
        if broken_line[1].startswith('$'):
            if broken_line[1][1] != '-':
                print(f"Interpreter error at: {line}, Unexpected character after stack reference.");
                break;
            else:
                if output_index < int(broken_line[1][2]):
                    print(f"Interpreter error at: {line}, Reference to stack is out of bounds. Negative index for return array.");
                    break;
                val1 = output[output_index - int(broken_line[1][2])];
                if not broken_line[3].startswith('$'):
                    val2 = int(broken_line[3]);
        
        if broken_line[3].startswith('$'):
            if broken_line[3][1] != '-':
                print(f"Interpreter error at: {line}, Unexpected character after stack reference.");
                break;
            else:
                if output_index < int(broken_line[3][2]):
                    print(f"Interpreter error at: {line}, Reference to stack is out of bounds. Negative index for return array.");
                    break;
                if not broken_line[1].startswith('$'):
                    val1 = int(broken_line[1]);
                val2 = output[output_index - int(broken_line[3][2])];
        
        if broken_line[1] in const:
            val1 = const[broken_line[1]];
            if not broken_line[3] in const:
                val2 = int(broken_line[3]);
        if broken_line[3] in const:
            val2 = const[broken_line[3]];
            if not broken_line[1] in const:
                val1 = int(broken_line[1]);

        if not broken_line[1].startswith('$') and not broken_line[3].startswith('$'):
            if broken_line[1] not in const and broken_line[3] not in const:
                val1 = int(broken_line[1]);
                val2 = int(broken_line[3]);
        
        operand = broken_line[2];
        match operand:
            # Start basic operators
            case '+':
                output[output_index] = val1 + val2;
            case '-':
                output[output_index] = val1 - val2;
            case '/':
                output[output_index] = val1 / val2;
            case '*':
                output[output_index] = val1 * val2;
            case '&':
                output[output_index] = val1 & val2;
            case '%':
                output[output_index] = val1 % val2;
            case '^':
                output[output_index] = val1 ** val2;
            case "==":
                output[output_index] = val1 == val2;
            case "!=":
                output[output_index] = val1 != val2;
            case '<':
                output[output_index] = val1 < val2;
            case '>':
                output[output_index] = val1 > val2;
            case ">=":
                output[output_index] = val1 >= val2;
            case "<=":
                output[output_index] = val1 <= val2;
            
            #End basic operators

            #TODO: Implement more advanced operators
            
            case _:
                print(f"Interpreter error at: {line}, Unknown operator.");
                exit();
        
        output_index += 1;
    
    elif line_return_type == "str":
        if len(broken_line) > 2:
            temp = "";
            i = 0;
            while i < len(broken_line) - 1:
                temp += broken_line[i+1] + ' ';
                i += 1;
            if temp.endswith(" "):
                # Removes the last character from the string. This means that we remove the unwanted whitespace at the trailing end of the string.
                temp = temp[:-1];
            output[output_index] = temp;
        else:
            output[output_index] = broken_line[1];

        output_index += 1;

    # This wont support whitespaces such as " " (space) at the moment.
    elif line_return_type == "char":
        if len(broken_line) > 2:
            print(f"Interpreter error at: {line}, Char type input is longer than expected.");
            break;
        elif len(broken_line[1]) > 1:
            print(f"Interpreter error at: {line}, Char type input is not a char it is a string.");
            break;

        output[output_index] = broken_line[1];
        output_index += 1;


print(f"Output array: {output}");
