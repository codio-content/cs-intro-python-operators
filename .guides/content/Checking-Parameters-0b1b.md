## Checking Parameter Data Types

Functions can fail with the wrong data type is passed as a parameter. The function definition below expects two numbers, but the function calls passes a string.

```python
def addition(num1, num2):
    """Add the two parameters together"""
    print(num1 + num2)
    
addition(5, "cat")
```

{try it}(python3 code/functions/check-parameters.py 1)

This code generates a type error. Python says the `+` operator cannot work with operands (the items being used with `+`) of type string. The program terminates with a cryptic error message. The `try... except` keywords allow for a more user-friendly error message.

![Try Except](.guides/images/try-except.png)

```python
def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any errors"""
    try:
        print(num1 + num2)
    except:
        print("There is an error in your code.")
    
addition(5, "cat")
```

{try it}(python3 code/functions/check-parameters.py 2)

Notice that a green check mark appears even though there is an error in the function call. `try... except` keeps the program running while providing feedback to the user.

<details><summary>**Failing Gracefully**</summary>No computer program works as intended 100% of the time. It is a good idea to design your code to "fail gracefully". That is, your program should not come crashing to a halt with each error. Think of ways that your program can roll with the punches even when mistakes happen.</details>

|||challenge
## What happens if you:
* Change the function call to `addition(5, 3)`?

|||

{try it}(python3 code/functions/check-parameters.py 3)

## Error Types

The code above provides an error message that is easy to understand, but it is not very helpful. What exactly is the problem? Python allows you to customize the exception messages based on the type of error. Trying to add a string to an int causes a type error, so the exception and message should reflect this.

```python
def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any type errors"""
    try:
        print(num1 + num2)
    except TypeError:
        print("Please pass the function two numbers")
    
addition(5, "cat")
```

{try it}(python3 code/functions/check-parameters.py 4)

<details><summary>**Python Errors**</summary>There are many kinds of [errors](https://docs.python.org/3/tutorial/errors.html) that can be used with the `except` keyword, but here is a list of some of the more common ones:<ul><li>**SyntaxError** - Incorrect syntax; missing parentheses for example</li><li>**ZeroDivisionError** - Divide a number by zero</li><li>**NameError** - Reference a variable that has not been declared</li><li>**TypeError** - Function or operation is applied to an incorrect type</li><li>**IndexError** - Reference an index that is out of range</li></ul></details>

|||challenge
## What happens if you:
* Change the print statement in the `try` block to `print(num1 + num3)`?

|||

{try it}(python3 code/functions/check-parameters.py 5)

{Check It!|assessment}(multiple-choice-1122179925)
