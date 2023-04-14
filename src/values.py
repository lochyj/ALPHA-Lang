# Example variable: "a": {"value": 10, "type": "int"},
variables = {};

# Example function: 
# "add": {
#   "inputs": {
#       "x": "int", 
#       "y": "int"
#   }, 
#   "function_string": {
#       "return": {"input": "x", "operation": "+", "input": "y"}
#   }
# }

# Example function: 
# "increase_money": {
#   "inputs": {
#       "increase_amount": "int"
#   }, 
#   "function_string": {
#       0: {"variable": "money", "operation": "+=", "input": "increase_amount"}
#   }
# }

# 0: is the line of the function
# "return": is indicating that the function will return this value

# This should be used for variable values when the variable is defined in evaluate(string: str)

functions = {};

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