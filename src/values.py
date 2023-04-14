# Example variable: "a": {"value": 10, "type": "int"},
variables = {};

# characters that cannot be in function, variable or datatype identifier. There is a special case for functions as they require () to define inputs.
special_characters = [
    "[",
    "]",
    "{",
    "}",
    ";",
    "/",
    "\\",
    "(",
    ")"
];

types = {
    "int": {},
    "char": {},
    "string": {},
    "null": {},     # This is the equivalent to void in c
}