----------

## What is a List Method?

Strings have special commands called methods (more on methods in a later lesson). Methods have a special syntax. First, start with a string (often a variable that represents a string). Add a period after the string. Finally, add the name of the method with any parameters. Parameters are values that the method will use.

![String Method with Parameters](.guides/images/string-method-parameters.png)

**Translation:** Remove the string `"world"` from the string `my_string`.

## The Strip Method

The `strip` method removes characters from the beginning or end of a string. `strip` returns a modified copy of the original string.

```python
string1 = "Hello world"
string2 = "world"
print(string1.strip(string2))
```

{try it}(python3 code/strings/strip-method.py 1)

|||challenge
## What happens if you:
* Change `string2` to `"Hello"`?
* Change `string2` to `"ld"`?
* Change `string2` to `"ell"`?

|||

{try it}(python3 code/strings/strip-method.py 2)

{Check It!|assessment}(multiple-choice-3496110909)
