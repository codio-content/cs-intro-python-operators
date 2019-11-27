----------

## Function Syntax

You have seen and used built-in functions like the length function (`len(my_list)`). This unit deals with user-defined function. Functions are composed of two parts, the header and the body.

![Fuction Header & Body](.guides/images/function-header-body.png)

The function header contains the `def` keyword which signals the definition of a function. Next is the name of the function. Function names follow the same rules as variable names; letters, numbers, and underscores. Function names cannot start with a number. Parentheses are required, and any parameters go between them. Finally, the header ends with a colon.

![Function Header](.guides/images/function-header.png)

The function body is the list of actions the function performs. All of the code for the function body must be indented (four spaces is the Python standard) from the function header. The function ends when the code is no longer indented.

![Function Body](.guides/images/function-body.png)

## Calling a Function

Enter the code below into the editor and click the `TRY IT` button. Nothing is printed. Defining a function does not cause Python to run it.

```python
def greet_twice():
    print("Hello")
    print("Hello")
```

{try it}(python3 code/functions/call-function.py 1)

You have to explicitly call the function if you want it to run. Add `greet_twice()` after the function definition. Remember **do not** indent the function call. Run the code again.

```python
def greet_twice():
    print("Hello")
    print("Hello")
    
greet_twice()
```

{try it}(python3 code/functions/call-function.py 2)

|||challenge
## What happens if you:
* Add another line code that says `greet_twice()`?
* Indent `greet_twice` four spaces?
* Add a `1` between the parentheses of the function call `greet_twice(1)`?

|||

{try it}(python3 code/functions/call-function.py 3)

{Check It!|assessment}(multiple-choice-1896286432)
