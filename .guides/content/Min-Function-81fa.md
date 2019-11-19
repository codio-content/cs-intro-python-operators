----------

## String Functions

String functions are predefined functions that perform an action on a string. Functions have a specific syntax — function name, parentheses, and a string (often a variable) between the parentheses. The string between the parentheses is called a parameter, which is a piece of information the function requires so it can do its job.

![String Function Syntax](.guides/images/string-function-syntax.png)

In fact, `len` is a string function. There are a few other functions that work with strings.

## The Min Function

The `min` function returns the "smallest" character from a string. Often times this is the character that appears first in alphabetical order. When characters are numbers and symbols, things are not so clear.

```python
my_string = "abcdefghijklmnopqrstuvwxyz"
print(min(my_string))
```

{try it}(python3 code/strings/min-function.py 1)

|||challenge
## What happens if you:
* Change `my_string` to `"AaBbCcDd"`?
* Change `my_string` to `"The brown dog jumps over the lazy fox."`?
<details><summary>**Note**</summary>The program does not have an error. You do not see anything because the "smallest" character is the " " between words. You cannot easily see a blank space on its own, which is why it seems like there is a problem with your code.</details>
* Change `my_string` to `"@<#$%!^&*="`?

|||

{try it}(python3 code/strings/min-function.py 2)

{Check It!|assessment}(multiple-choice-1321912568)

