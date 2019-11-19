----------

## The Replace Method

The `replace` method returns a copy of the original string in which part of the original string (also called a substring) has been replaced with another set of characters.

```python
my_string = "dog mouse fish dog bear"
new_string = my_string.replace("dog", "cat")
print(new_string)
```

{try it}(python3 code/strings/replace-method.py 1)

|||challenge
## What happens if you:
* Change `my_string` to `"dogmousefishdogbear"`?
* Change `new_string` to `"my_string.replace("Dog", "cat")`?
* Change `new_string` to `"my_string.replace("dog", "cat", 1)`?

|||

{try it}(python3 code/strings/replace-method.py 2)

{Check It!|assessment}(fill-in-the-blanks-1923077265)
