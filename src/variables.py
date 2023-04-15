import src.values as values

# int a = 10 + 10;

# int a = 10;
# Example variable: "a": {"value": 10, "type": "int"},

# TODO: allow for the redefinition of variables inside of function that are local...
# Maybe have a IsInsideFunction bool in values.py that also has the local vars stored in functions var
# if IsInsideFunction:
#    ... = functions[fn_name]["locals"][var_name]
# And have it access this first before looking for global vars.

def evaluate(sample: str) -> any:
    # Need to allow for replacement of variables's with their respective values. Try using a similar thing to what we have for functions
    exec(f"global res; res = {sample}", globals());
    return res;

def define_variable(line: list[str]):
    var_type = line[0];
    var_name = line[1];

    if var_type not in values.types.keys():
        print(f"Interpreter error: {line}, Unknown type '{var_type}'");
        exit();

    var_eval_string = "";

    skip = 3;
    for obj in line:
        if skip > 0:
            skip -= 1;
            continue;

        if obj.endswith(';'):
            obj = obj[:-1];

        var_eval_string += f"{obj} ";

    if (var_name in values.variables.keys()):
        print(f"Interpreter error: {line}, Redefinition of already defined variable.")
        exit();    
    
    var_value = evaluate(var_eval_string);

    if var_type == "int":
        var_value = int(var_value);

    values.variables.update({var_name: {"value": var_value, "type": var_type}});


# TODO: Finish this
def update_variable(line: list[str]):
    var_name = line[1];

    if var_name not in values.variables.keys():
        print(f"Interpreter error: {line}, Cannot assign value to an undefined variable. Try:");
        print(f"auto {line}");      #TODO: add auto type
        print(f"~~~~");
        exit();

    var_eval_string = "";

    skip = 2;
    for obj in line:
        if skip > 0:
            skip -= 1;
            continue;

        if obj.endswith(';'):
            obj = obj[:-1];

        var_eval_string += f"{obj} ";

    if (var_name in values.variables.keys()):
        print(f"Interpreter error: {line}, Redefinition of already defined variable.");
        exit();
    
    var_value = evaluate(var_eval_string);

    if values.variables[var_name]["type"] == "int":
        var_value = int(var_value);

    values.variables[var_name].update({"value": var_value});