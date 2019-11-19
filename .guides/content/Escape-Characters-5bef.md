----------

## Escape Characters

An escape character is a character that has a different interpretation that what you see in a string. Escape characters always start with a backslash (`\`). The most common escape character is the newline character (`\n`) which causes Python to print on the next line.

```python
my_string = "Hello\nworld"
print(my_string)
```

{try it}(python3 code/strings/escape-characters.py 1)

|Escape Character|Description|Example|
|----------------|-----------|-------|
|**\\\\**|Prints a backslash|`print("\\")`|
|**\\\'**|Prints a single quote|`print("\'")`|
|**\\\"**|Prints a double quote|`print("\"")`|
|**\\\t**|Prints a tab (spacing)|`print("Hello\tworld")`|
|**\\\uxxxx**|Prints a [hexidecimal unicode character](https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples)|`print("\u26BE")`|

|||challenge
## What happens if you:
* Use `\n\n` instead of `\n`?
* Replace the `\n\n` with `\t`?
* Find a hexidecimal unicode character to use (see link above)?

|||

{try it}(python3 code/strings/escape-characters.py 2)

## Quotes Inside Quotes

Imagine that you have this small bit of dialog, `And then she said, "Hi there."` and want to store it as a string. Typing `"And then she said, "Hi there.""` would cause an error.

![Quote in a Quote Wrong](.guides/images/quote-in-quote-wrong.png)

When you use a `"` to start a string, Python looks for the next `"` to end it. To avoid syntax errors, you can use a double quote to start your string, single quotes for the inner quote, and end the string with a double quote.

```python
my_string = "And then she said, 'Hi there.'"
print(my_string)
```

{try it}(python3 code/strings/escape-characters.py 3)

|||challenge
## What happens if you:
* Use single quotes (`'`) on the outside and double quotes (`"`) on the inside?
* Use only single quotes (`'`)?
* Use the escape character `\"` for the inner quotation marks?

|||

{try it}(python3 code/strings/escape-characters.py 4)

{Check It!|assessment}(multiple-choice-2648320213)

