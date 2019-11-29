----------

## Named Parameters

Typically, parameter values are assigned based on their position in the function call. However, Python allows you to pass a value to a parameter based its name.

```python
def subtract(num1, num2):
    """Subtract the second parameter from the first"""
    print(num1 - num2)
    
subtract(5, 2)
subtract(2, 5)
subtract(num2=2, num1=5)
```

{try it}(python3 code/functions/parameter-values.py 1)

|||challenge
## What happens if you:
* Change the function call to `subtract(num3=2, num1=5)`?
* Change the function call to `subtract(num1=2, 5)`?
* Change the function call to `subtract(num1=2, num1=5)`?

|||

{try it}(python3 code/functions/parameter-values.py 2)

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

{try it}(python3 code/functions/parameter-values.py 3)

|||challenge
## What happens if you:
* Change the function call to `parameter_types([1,2,3], -6, len, True)`?
* Change the function call to `parameter_types(range(10), "", parameter_types, 45)`?

|||

{try it}(python3 code/functions/parameter-values.py 4)

{Check It!|assessment}(multiple-choice-1415019255)
