----------

## The Starts With Method

The `startswith` method returns either `True` or `False` if a string starts with another string. For example, `my_string.startswith("this")` will return `True` if `my_string` starts with `"this"`. If not, it will return false. The `startswith` method is a bit different because some of the parameters are optional. The first parameter, a string, is mandatory. `startswith` will start the comparison with the first character in the string. However, you can change where the comparison starts and ends with the optional parameters. 

![Optional Parameters](.guides/images/string-method-optional-parameters.png)

```python
my_string = "this is a string"
my_bool = my_string.startswith("this")
print(my_bool)
```

{try it}(python3 code/strings/startswith-method.py 1)

|||challenge
## What happens if you:
* Change `my_bool` to `my_string.startswith("This")`?
* Change `my_bool` to `my_string.startswith("is", 2)`?
* Change `my_bool` to `my_string.startswith("is", 2, 3)`?
* Change `my_bool` to `my_string.startswith("is", 2, 4)`?

|||

{try it}(python3 code/strings/startswith-method.py 2)

{Check It!|assessment}(fill-in-the-blanks-1792875991)
