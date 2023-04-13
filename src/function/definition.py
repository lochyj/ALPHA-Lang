import src.values as values
# fn int add (x,y) x + y;

def create_function(fn_name: str, fn_vars: str, fn_string: str):
    bracket_open = "{"
    bracket_close = "}"
    # Sorry for this abomination
    exec(f"global {fn_name}_ext\ndef {fn_name}_ext ({fn_vars}): {fn_string}", globals());
    exec(f"values.fn_user.update({bracket_open}'{fn_name}': {fn_name}_ext{bracket_close})", globals());

def parse_line_fndefinition(line: str):
    split_line = line.split(' ');

    fn_name = split_line[2].replace('(', ' ').split(' ')[0];

    if fn_name in values.fn_user.keys():
        print(f"Interpreter error at: {line}, Redefinition of previously defined function.");
        exit();
    
    fn_string = "";
    
    fn_vars = {};
    var_index = 0;

    if split_line[3].startswith('('):
        for char in split_line[3]:
            if char == ')':
                break;
            elif char == '(':
                continue;
            elif char == ',':
                var_index += 1;
                continue;
            else:
                if var_index in fn_vars.keys():
                    fn_vars[var_index] += char;
                else:
                    fn_vars.update({var_index: char});
    else:
        print(f"Interpreter error at: {line}, Unknown symbol at function definition.");
    fn_input_vars = "";
    index = 0;
    while index < len(fn_vars.keys()):
        fn_input_vars += fn_vars[index] + ","
        index += 1;
    fn_input_vars = fn_input_vars[:-1]

    split = 4;
    while split < len(split_line):
        fn_string += f"{split_line[split]} ";
        split += 1;

    create_function(fn_name, fn_input_vars, fn_string)
