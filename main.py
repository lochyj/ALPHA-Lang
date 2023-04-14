import src.values as values
from src.util import *

file = open("file.mid");
file_contents = file.read();

split_line = file_contents.replace('\n', ' ').split(' ');

defining_var = False;
defining_function = False;

i = 0;
while i < len(split_line):
    if split_line[i] == '':
        i += 1;
        continue;
    
    symbol = split_line[i];

    if symbol in values.types.keys():
        if split_line[i + 2] == "=":
            defining_var = True;
        elif split_line[i + 2] == "(":
            defining_function = True;

    if defining_var:
        var_type = symbol;
        var_name = split_line[i + 1];
        # TODO: evaluate the value
        var_value = "";
        val_index = 0;
        val_defs = True;
        eval_string = "";
        while val_defs:
            if split_line[i + 3 + val_index].endswith(';'):
                eval_string += f"{split_line[i + 3 + val_index].replace(';', '')} ";
                val_defs = False;
                continue;
            eval_string += f"{split_line[i + 3 + val_index]} ";
            val_index += 1;

        # Currently doesn't support variables within the definition of variables
        var_val = evaluate(eval_string);
        if var_name in values.variables.keys():
            # TODO: Make this look better
            interpreter_error(f"{split_line}", "Redefinition of predefined variable.")
        values.variables.update(construct_var(var_name, var_val, var_type));
        print(values.variables)
        defining_var = False;
    elif defining_function:
        print("Unimplemented...")
    
    i += 1;