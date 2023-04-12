from src.builtin import *

global types;
types = [
    "int",
    "char",
    "str",
    "arr",
    "fn"
];

global fn_types;
fn_types = [
    "null",
    "int",
    "char",
    "arr",
    "str"
];

global const;
const = {
    "PI": 3.1415926,
    "E": 2.7182818
};

global fn_builtins;
fn_builtins = {
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "print": print,
    "log": log,
    "log10": log10,
    "sqrt": sqrt,
    "ceil": ceil,
    "abs": abs
};

global fn_user;
fn_user = {};

global output;
output = {};

global output_index;
output_index = 0;