----------

## Parameters

Parameters are required values passed to a function. The function uses the parameters to accomplish the stated goal in the docstring. In the example below, the function adds the parameters together. Parameters are those values in between the parentheses. If your function uses parameters, they need to be present when you define and call the function. Multiple parameters are separated by commas.

![Parameters](.guides/images/parameters.png)

```python
def addition(num1, num2):
    """Prints the sum of two numbers"""
    print(num1 + num2)

addition(5, 7)
```

{try it}(python3 code/functions/parameters.py 1)

|||challenge
## What happens if you:
* Change the function header to `def addition(num1):`?
* Change the function call to `addition()`?
* Change the function call to `addition(5, 10, 15)`?

|||

{try it}(python3 code/functions/parameters.py 2)

## Parameters as Variables

You can think of parameters as variables. They are declared in the function header, and their values are determined by the function call. Because of this, the order of parameters is important. The first parameter in the function call will be the first parameter in the function header, the second parameter from the function call will be the second parameter in the function header, etc.

![Parameter Order](.guides/images/parameter-order.png)

```python
def add_sub(num1, num2, num3):
    """add_sub does the following:
    Add the first two parameters
    Subtract the third paramter
    Print the result"""
    print(num1 + num2 - num3)

add_sub(5, 10, 15)
```

{try it}(python3 code/functions/parameters.py 3)

|||challenge
## What happens if you:
* Change the function call to `add_sub(10, 15, 5)`?
* Change the function call to `add_sub(15, 5, 10)`?

|||

{try it}(python3 code/functions/parameters.py 4)

Insert reading question
