----------

## Parameter Values

If parameters can be thought of as variables, then they can have the same values as variables: ints, floats, strings, boolean, lists, etc.

```python
def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each element"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))
        
parameter_types(1, 5.9, "Beatles", False)
```

{try it}(python3 code/functions/parameter-values.py 1)

|||challenge
## What happens if you:
* Change the function call to `parameter_types([1,2,3], -6, len, True)`?
* Change the function call to `parameter_types(range(10), "", parameter_types, 45)`?

|||

{try it}(python3 code/functions/parameter-values.py 2)

## Expressions as Parameters

Functions can even accept expressions as parameters. `5 + 7`, `100 < 80`, and `int("32")` are all examples of expressions. Since these expression result in a data type that can be used as a parameter, the expression itself can be passed as a parameter.

```python
Example code
```

{try it}(python3 code/functions/parameter-values.py 3)

|||challenge
## What happens if you:
* Code suggestion
* Code suggestion

|||

{try it}(python3 code/functions/parameter-values.py 3)

Insert reading question
