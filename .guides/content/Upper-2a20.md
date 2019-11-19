----------

## The Upper Method

There are some string methods that do not require parameters. You still must use the parentheses even if there are no parameters. The `upper` method is an example of this. The `upper` method returns a copy of the original string with all uppercase characters.

![String Method with No Parameters](.guides/images/string-method-no-parameters.png)

**Translation:** Convert all the characters of `my_string` to uppercase.

```python
my_string = "the big brown dog"
print(my_string.upper())
```

{try it}(python3 code/strings/upper-method.py 1)

|||challenge
## What happens if you:
* Change `my_string` to `"ThE bIg BrOwN dOg"`?
* Change `my_string` to `"THE BIG BROWN DOG"`?
* Change `my_string` to `"123!@#"`?

|||

{try it}(python3 code/strings/upper-method.py 2)

{Check It!|assessment}(multiple-choice-2673636806)
