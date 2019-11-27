----------

## Function Documentation

Python has a built-in function called `help` that explains how other functions work. This is a handy way of learning how to use a function without having to look it up in the official documentation. 

```python
help(len)
```

{try it}(python3 code/functions/docstring.py 1)

|||challenge
## What happens if you:
* Replace `len` with `max`?
* Change the code to look like this:
```python
def greet_twice():
    print("Hello")
    print("Hello")
    
help(greet_twice)
```

|||

{try it}(python3 code/functions/docstring.py 2)

## Docstring

The `help` function does not provide any information for user-defined functions. Add a docstring to a user-defined function will provide output for the `help` function. A docstring goes between the function header and the function body. Use triple-quotes to create a string which explains what the function does and how to use it. Remember, triple-quotes respect all of the whitespace in the string. You can indent or and to a new line to increase readability.

![Docstring](.guides/images/docstring.png)

```python
def greet_twice():
    """Print the string 'Hello' two times"""
    print("Hello")
    print("Hello")
    
help(greet_twice)
```

{try it}(python3 code/functions/docstring.py 3)

|||challenge
## What happens if you:
* Remove the indentation for the docstring?
* Indent the docstring and then change it to:
```python
"""Print the string
'Hello' two times"""
```
* Change the docstring to `"Print the string 'Hello' two times"`?
* Change the docstring to:
```python
"Print the string
'Hello' two times"
```

|||

{try it}(python3 code/functions/docstring.py 4)

{Check It!|assessment}(multiple-choice-1804598706)
