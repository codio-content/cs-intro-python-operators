----------

## Side Effects

Side effects are any changes that a function produces that are external to the function itself. Examples of side effects are printing to the screen, changing a global variable, writing to a file, etc. Sometimes side effects are the desired outcome, but there are many programmers who believe that functions should not have side effects (these are called pure functions). The examples below demonstrate how to incorporate pure functions into programs that have side effects.

### Modify a Global Variable

Global variables can be modified by a function without using the `global` keyword, which is a side effect. In the for loop, the new value of `my_num` is calculated by calling the function `add_5`. You can see the value of `my_num` change each time the loop runs.

```python
my_num = 0

def add_5(num):
    """Receive a number, add 5 tot the number, and
    return the new number"""
    return(num + 5)
  
for i in range(10):
    my_num = add_5(my_num)
    print(my_num)
```

{try it}(python3 code/functions/side-effects.py 1)

|||challenge
## What happens if you:
* Change the program to look like this:
```python
def add_5():
    """Add 5 to my_num and return the new number"""
    return(my_num + 5)
  
for i in range(10):
    my_num = add_5()
    print(my_num)
```
<details><summary>**Why the above code is not preferred**</summary>The code where `add_5` has no parameters produces the exact same output as the code where `add_5` has a parameter. However, the code where `add_5` has a parameter is preferable to the code where `add_5` does not have a parameter. The function without the parameter relies on the global variable `my_num`. If you were to copy/paste this function into another program, it would only work if there was a global variable named `my_num`. The function with the parameter, however, will work in used in another program. Having the parameter means the function is not dependent upon specific global variables. This reduces the chance for an error.</details>

|||

{try it}(python3 code/functions/side-effects.py 2)

### Printing

The code below prints if a number is odd or even. The first function determines if a number is odd or even. The second function constructs the appropriate string. Neither function has a side effect. The act of printing is left to the main program.

```python
def is_even(num):
    """Return True if num is even
    return False if num is odd"""
    return num % 2 == 0
  
def output(num):
    """Return a string with a number,
    and states if that number is even or odd"""
    if is_even(num):
        return "{} is an even number.".format(num)
    else:
        return "{} is an odd number.".format(num)
  
print(output(2))
```

{try it}(python3 code/functions/side-effects.py 3)

|||challenge
## What happens if you:
* Change the print statement to `print(output(3))`?

|||

{try it}(python3 code/functions/side-effects.py 4)

### Are Side Effects Bad?

No, side effects are not bad. In fact, they may be the desired result. However, the more side effects a function produces, the greater the risk of introducing a bug. Think about the functions you are writing. If possible, break up your code into several smaller functions, and only introduce side effects when necessary. This may mean you have to write more code, but if this keeps you from having to spend a lot of time debugging, then it it time well spent.

{Check It!|assessment}(multiple-choice-511526029)
