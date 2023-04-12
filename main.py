from src.values import *
from src.parse import *

file = open("test.a");
file_contents = file.read();
file_lines_array = file_contents.splitlines();


for line in file_lines_array:
    parse_line(line);
    continue;
    
    # This wont support whitespaces such as " " (space) at the moment.

    if line_return_type == "fn":
        val = 0;
        
        if broken_line[2].startswith('$'):
            if broken_line[2][1] != '-':
                print(f"Interpreter error at: {line}, Unexpected character after stack reference.");
                break;
            else:
                if output_index < int(broken_line[2][2]):
                    print(f"Interpreter error at: {line}, Reference to stack is out of bounds. Negative index for return array.");
                    break;
                else:
                    val = output[output_index - int(broken_line[2][2])];
        
        if broken_line[2] in const:
            val = const[broken_line[2]];

        if not broken_line[2].startswith('$'):
            if broken_line[2] not in const:
                val = broken_line[2];

        if broken_line[1] not in fn_types:
            if broken_line[1] in fn_builtins:
                tmp = fn_builtins[broken_line[1]](val);
                if tmp != None:
                    output[output_index] = tmp;
                    tmp = None;
                    output_index += 1;
            elif broken_line[1] in fn_user:
                tmp = fn_user[broken_line[1]](val);
                if tmp != None:
                    output[output_index] = tmp;
                    tmp = None;
                    output_index += 1;
            else:
                print(f"Interpreter error at: {line}, Unknown function call; Function neither builtin nor user defined.");
                break;
        elif broken_line[1] in fn_types:
            print(f"Interpreter error at: {line}, Function definitions aren't implemented yet.");
            break;
        else:
            print(f"Interpreter error at: {line}, Missing function call or definition.");
            break;
        output_index += 1;
        

print(f"Output array: {output}");
