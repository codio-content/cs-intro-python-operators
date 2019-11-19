----------

## While Loop

String iteration is most often done with a for loop. However, a while can be used as well.

```python
my_string = "Calvin and Hobbes"
length = len(my_string)
i = 0

while i < length:
    print(my_string[i])
    i += 1
```

[Code Visualizer](open_tutor code/strings/string-while-loop.py)
{try it}(python3 code/strings/string-while-loop.py 1)

|||challenge
## What happens if you:
* Change the loop to `while i <= length:`?
* Change the `print` statement to `print(i)`?
* Remove `i += 1`?

|||

{try it}(python3 code/strings/string-while-loop.py 2)

## Comparing While & For Loops

![Compare While & For Loops](.guides/images/compare-for-while-loops-strings.png)

The for loop is more efficient than a while loop when iterating over a string. You do not need to declare variables for the length of the string (red text), declare a variable for the index of the string (blue text), or increment the index variable (orange text). All of this is handled by the `in` statement. In for loops, you can use the iteration variable to reference the string character. With a while loop, however, you need to use the string and index to reference the character (purple text).

{Check It!|assessment}(fill-in-the-blanks-172748421)
