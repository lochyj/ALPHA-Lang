import src.values as values
# fn int add(x,y) x + y;
def parse_line_fndefinition(line: str):
    split_line = line.split(' ');

    fn_name = split_line[2].replace('(', ' ').split(' ')[0];

    if fn_name in values.fn_user.keys():
        print(f"Interpreter error at: {line}, Redefinition of previously defined function.");
        exit();
    fn_call: function = ...;
    exec(f"global {fn_name}_ext\ndef {fn_name}_ext (x, y): return x + y;", globals());
    exec(f"global fn_call\nfn_call = {fn_name}_ext", globals());
    
    fn_vars = [];
    fn_vars_index = 0;

    if split_line[2].find('(') == -1:
        ...
    elif split_line[3].startswith('('):
        ...

    


    values.fn_user.update({fn_name: fn_call});
    print(values.fn_user)
    print(f"Interpreter error at: {line}, Function definitions are yet to be implemented.");

