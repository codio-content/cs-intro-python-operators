----------

## String Interpolation

String interpolation is the process of putting the value of a variable inside of a string. You have already practiced a form of string interpolation by using `+` and type casting.

```python
arms = 2
fingers = 10
print("I have " + str(arms) + " arms and " + str(fingers) + " fingers.")
```

{try it}(python3 code/strings/string-interpolation.py 1)

## Comma-Separated String Interpolation

Another way to do string interpolation is to use commas instead of the `+` operator.

```python
verb = "jumps"
adjective = "lazy"
print("The brown dog ", verb, " over the ", adjective, " fox.")
```

{try it}(python3 code/strings/string-interpolation.py 2)

|||challenge
## What happens if you:
* Change `verb` to `5`?
* Use commas for the variable `verb` and the `+` operator for `adjective`?
* Change `adjective` to `True`?

|||

{try it}(python3 code/strings/string-interpolation.py 3)

{Check It!|assessment}(multiple-choice-4155035086)

