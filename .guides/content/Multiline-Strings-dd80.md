----------

## Multiline Strings

Python has several informal rules. Breaking one of these will not cause an error, but the Python community will not consider the code to be "proper". One of these rules is that a line of text should not have more than 79 characters. If a string has more than 79 characters, use the newline character (` \`) and go to the next line. Note, Python will print the string as one line of text.

```python
my_string = "Hello world! This is a very, very long string. \
Even though this string is on three different lines, it should \
print as one line. Notice how the line breaks are different."
print(my_string)
```

{try it}(python3 code/strings/string-multiline.py 1)

|||challenge
## What happens if you:
* Put a space after the `\`?

|||

{try it}(python3 code/strings/string-multiline.py 2)

## Triple Quotes

Triple quotation marks can be used to preserve the whitespace of a string.

```python
long_string = """Notice how this weird looking
    string is being
        printed."""
print(long_string)
```

{try it}(python3 code/strings/string-multiline.py 3)

<details><summary>**Docstrings**</summary>The triple quote (`"""`) has a special purpose, documenting code. You will learn more about docstrings in the lessons on functions and classes.</details>

|||challenge
## What happens if you:
* Change the `"""` to `'''`?
* Have `"""` to start the string and `'''` to end the string?

|||

{try it}(python3 code/strings/string-multiline.py 4)

{Check It!|assessment}(multiple-choice-2380152059)
