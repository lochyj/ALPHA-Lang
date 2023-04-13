from src.values import *
from src.types.int import parse_line_int
from src.types.str import parse_line_str
from src.types.char import parse_line_char
from src.function.fn import parse_line_fncall
from src.function.definition import parse_line_fndefinition

def skip_line(line: str):
    if line == '':
        return True;
    elif line.strip().startswith("//"):
        return True;

    split_line = line.split(' ');
    
    if split_line[0] not in types:
        print(f"Interpreter error at: {line}, Missing type definition.");
        exit();

    return False;

def parse_line(line: str):
    if skip_line(line):
        return;

    split_line = line.split(' ');
    return_type = split_line[0];

    match return_type:
        case "int":
            parse_line_int(line);
        case "str":
            parse_line_str(line);
        case "char":
            parse_line_char(line);
        case "fn":
            if split_line[1] not in fn_types:
                parse_line_fncall(line);
            elif split_line[1] in fn_types:
                parse_line_fndefinition(line);
