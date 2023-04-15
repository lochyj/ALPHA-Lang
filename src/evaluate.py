import src.values as values

# "increase_money": {
#   "inputs": {
#       "increase_amount": "int"
#   }, 
#   "function_string": {
#       0: {"variable": "money", "operation": "+=", "input": "increase_amount"}
#   }
# }

def evaluate_function_string(fn_string: str):
    

# print "Hello, World!"
def call_function(line: list[str]):
    if line[0] not in values.functions.keys():
        print(f"Interpreter error: {line}, Call to unknown function.");
        exit();

