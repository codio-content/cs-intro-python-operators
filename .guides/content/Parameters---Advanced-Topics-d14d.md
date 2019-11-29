----------

## Optional Parameters

Python allows you to create functions with optional parameters. They are considered to be optional because the function call can state the parameter or not. However, the function declaration will name this parameter and give it a default value.

![Optional Parameters](.guides/images/optional-parameters-declaration.png)

```python
def add_if_true(num1, num2, bool = True):
    """Prints the sum of two numbers
    if the variable bool is true"""
    if bool:
        print(num1 + num2)
    else:
        print("No addition, bool is false")

add_if_true(5, 7)
add_if_true(5, 7, False)
```

{try it}(python3 code/functions/advanced-parameters.py 1)

|||challenge
## What happens if you:
* Add a function call that looks like this `add_if_true(29, 45, True)`?

|||

{try it}(python3 code/functions/advanced-parameters.py 2)

## Variable Parameter Lists

It is possible to declare a function with a list of variables of an undetermined length. The function below will find the sum for any number passed as a parameter. There can be two parameters or twenty, but it is not necessary to write out each parameter. Instead, use a `*` before a single parameter name. This creates a list of parameters.

```python
def calc_sum(*nums):
    """Calculate the sum of all of the parameters"""
    total = 0
    for num in nums:
        total += num
    print(total)
    
calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

{try it}(python3 code/functions/advanced-parameters.py 3)

|||challenge
## What happens if you:
* Change the function call to `calc_sum(4)`?
* Change the function call to `calc_sum()`?

|||

{try it}(python3 code/functions/advanced-parameters.py 4)

{Check It!|assessment}(fill-in-the-blanks-3645586010)
