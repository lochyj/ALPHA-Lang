# The ALPHA programming language conventions

## Return types

The line return type is always the first thing in the line unless the line is a comment or a function
e.g:
```c
int 10 + 10
```
This specifies that the type of the line is an `int`eger and the value is `10 + 10`

For other types such as chars and strings we use the `char` and `str` keywords respectively. e.g:
```c
char a
// And
str Hello, World!
```
Note:
- The char type has to have only one input and that input must have a length of 1.
- The str type can have 1 or more inputs and it will combine them into one string.

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

Functions will be limited to one line only and will allow logical operations such as `if` and `while` statements. However i am yet to implement this.

Functions are defined with the `fn` type and will be placed before the return type of the function. e.g:
```rs
// Yet to implement the rest...
fn null ...
// Or
fn int ...
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

Additionally, for syntax highlighting the best language to use is `c` as it is the closest to the ALPHA language.