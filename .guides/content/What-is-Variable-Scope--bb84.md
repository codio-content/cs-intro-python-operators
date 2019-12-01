----------

## What is Variable Scope?

Variable scope is a concept that determines where a variable "exists" in your program. Look at the code below. There are two variables called `my_var`. One is the very first line of the program, and the other is inside a function. The program calls the function which assigns a value to and prints `my_var`, and then the program prints `my_var`.

Short introduction

```python
my_var = "outer scope"

def print_scope():
    my_var = "inner scope"
    print(my_var)

print_scope()
print(my_var)
```

{try it}(python3 code/functions/variable-scope.py 1)

Surprisingly, the output of this program is `inner scope` and `outer scope`. Variable scope explains why this is. The first `my_var` (the red one) exists only in the light red area. This is called global scope. The second `my_var` (the blue one) exists only in the light blue area. This is called local scope. Because of this, the blue `my_var` cannot overwrite the red `my_var` (or vice versa). The blue `my_var` is independent of the red `my_var`. That is why the output of the program is two different strings.

![Variable Scope](.guides/images/variable-scope.png)

|||challenge
## What happens if you:
* Add the parameter `my_var` to the `print_scope` function and pass `my_var` to `print_scope` in the function call?
```python
my_var = "outer scope"

def print_scope(my_var):
    my_var = "inner scope"
    print(my_var)

print_scope(my_var)
print(my_var)
```

|||

{try it}(python3 code/functions/variable-scope.py 2)

## Scope Resolution

The example above shows how variable scope keeps two variables with the same name independent from one another. Unfortunately, there is an exception to this rule. Take a look at the code below. There is a global variable `total`. It is not passed to the function and there is no variable `total` declared inside the function. Local versus global scope should keep `total` from "existing" in the function. This should be an error, right?

```python
total = 5

def augment_total(num):
    print(num + total)

augment_total(10)
```

{try it}(python3 code/functions/variable-scope.py 3)

The variable `total` has global scope, so it can be "seen" inside the function. As shown above, you cannot modify `total` from inside the function. This is called scope resolution. Scope resolution is a one-way street — global variables can be seen inside functions, but variables inside functions cannot be seen outside the function.

|||challenge
## What happens if you:
* Change the program to look like this:
```python
total = 5

def augment_total(num):
    x = 7
    print(num + total)

augment_total(10)
print(x)
```

|||

{try it}(python3 code/functions/variable-scope.py 4)

{Check It!|assessment}(fill-in-the-blanks-18589681)
