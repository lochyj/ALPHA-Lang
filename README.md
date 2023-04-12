# The ALPHA programming language conventions

## Return types

The line return type is always the first thing in the line unless the line is a comment or a function
e.g:
```c
int 10 + 10
```
This specifies that the type of the line is an integer and the value is `10 + 10`

For other types such as chars and strings we use the `char` and `str` keywords respectively. e.g:
```c
char a
// And
str Hello, World!
```
Note:
- The char type has to have only one input and that input must have a length of 1.
- The str type can have 1 or more inputs and it will combine them into one string.

## Mathematical, bitwise and comparison operators

In ALPHA we have the following mathematical, bitwise and comparison operators:
```c
int 10 + 10 // Addition
int 10 - 10 // Subtraction
int 10 * 10 // Multiplication
int 10 / 10 // Division
int 10 % 10 // Modulus
int 10 ^ 10 // Power
int 10 & 10 // Bitwise AND
int 10 | 10 // Bitwise OR
int 10 == 10 // Equals
int 10 != 10 // Not equals
int 10 < 10 // Less than
int 10 > 10 // Greater than
int 10 <= 10 // Less than or equal to
int 10 >= 10 // Greater than or equal to
```

## Stack references

In ALPHA there are not variables. Instead we use a "stack" like system where we can reference the output of a line by using the `$-` symbol. To get the return value we want to use we use the `$-` symbol and then the number of returns we want to go back. e.g:
```c
int 10 + 10
int $-1 + 10
```
This will return `20` and `30` respectively as the first line returns `20` and the second line will add `10` to the return value of the first line `$-1`.

More examples:
```c
int 10 + 10
// Returns 20
int $-1 + 10
// Returns 30
int $-2 + 10
// Returns 30 as we go back 2 returns which is the output of the first line
```

## Constants

As previously mentioned there are no variables in ALPHA. In programming you often need certain values that you don't really want to remember and add to your projects all of the time. For example: PI and e. We have constants for this. E.G:
```c
// Calculate the circumference of a circle with the radius of 10
int 2 * PI
int $-1 * 10
```

## Functions

Functions are limited to one line only and will allow logical operations such as `if` and `while` statements. However I am yet to implement function definitions

Functions are defined with the `fn` type and will be placed before the return type of the function. e.g:
```rs
// Yet to implement the rest...
fn null ...
// Or
fn int ...
// Or any other return type
```

To call a function you simply use the `fn` type and then the name of the function. e.g:
```rs
str Hello, world!
fn print $-1
```

In this case `print` is a builtin function that will print the value input to the console.

There are many other builtin functions. They will be continually added to in the future.
Here is the current list.<br>
```
sin
cos
tan
print
log
log10
sqrt
ceil
```

## Notes

Because this is a simple language we ALWAYS have to have spaces between the symbols. e.g:
```c
// Correct:
int 10 + 10

// Incorrect:
int 10+10
// Or 
int 10 +10
// Or any other combination of missing spaces
```

Additionally, for syntax highlighting the best language to use is `c` or `rust` as it is the closest to the ALPHA language.
E.g:<br>
`C`:
```c
int 10 + 10
fn print $-1
```
`Rust`:
```rs
int 10 + 10
fn print $-1
```