----------

## The Format Method

All of the quotation marks, commas, and `+` can get hard to read. So Python 3 introduced a new way to perform string interpolation. The `format` method lets you put a placeholder and then assign a variable to the placeholder.

![Format Method](.guides/images/string-interpolation-format.png)

The `{}` are placeholders for a variable, and after `format` there is a list of variables for the placeholders. Notice that the first variable goes into the first placeholder, the second variable into the second placeholder, etc.

```python
var1 = "today"
var2 = "luckiest"
print("Yet {} I consider myself the {} man on the face of this earth.".format(var1, var2))
```

{try it}(python3 code/strings/format-string-interpolation.py 1)

|||challenge
## What happens if you:
* Change `format` to read `format(var2, var1)`?
* Change `var1` to `5`?
* Change `var2` to `True`?

|||

{try it}(python3 code/strings/format-string-interpolation.py 2)

## Reorder the Variables

By default, the `format` method uses the order of variables (from left to right) when placing them into a placeholder. However, you can change the order variables by using an index. The first variable has an index of 0, the second and index of 1, etc.

![Rearrange Order](.guides/images/rearrange-string-interpolation-format.png)

```python
var1 = "today"
var2 = "luckiest"
print("Yet {1} I consider myself the {0} man on the face of this earth.".format(var1, var2))
```

{try it}(python3 code/strings/format-string-interpolation.py 3)

|||challenge
## What happens if you:
* Switch the `1` and the `0`?
* Change `1` to `2`?

|||

{try it}(python3 code/strings/format-string-interpolation.py 4)

{Check It!|assessment}(fill-in-the-blanks-1276437047)
