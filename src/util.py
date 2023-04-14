def interpreter_error(line: str, error: str):
    print(f"Interpreter error: {line} | {error}")
    exit();

def evaluate(sample: str) -> any:
    # Need to allow for replacement of variables's with their respective values

    # Pretty sure we only need one "global" specifier but having both works too so keep it safe.
    exec(f"global res; res = {sample}", globals());
    return res;

def construct_var(name: str, value: str, type: str):
    val: any = None;
    if type == "int":
        val = int(value);
    elif type != "int":
        val = value
    return {name: {"value": val, "type": type}}