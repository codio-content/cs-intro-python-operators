----------

## Type Casting
Type casting (or type conversion) is when you change the data type of a variable.

```python
a = 3
print(type(a))
a = str(a)
print(type(a))
```

<details><summary><b>What does </b><code>type</code> <b>mean?</b></summary>The <code>type</code> command returns the data type of the value stored in a variable. Python abbreviates these types: <code>int</code> is an integer, <code>float</code> is a floating point number, <code>str</code> is a string, and <code>bool</code> is a boolean.

{try it}(python3 code/operators/playground-type-cast.py 1)

`a` is initially an integer, but `str(a)` converted `a` into a string.

|||challenge
## What happens if you:
* Convert `a` to a floating point number?
* Convert `a` to a boolean?

|||

{try it}(python3 code/operators/playground-type-cast.py 2)

## Why Type Cast?
Do you know why the code below will not work?

```python
a = 5
b = "3"
print(a + b)
```

{try it}(python3 code/operators/playground-type-cast.py 3)

You cannot add a string to an integer. You can convert `b` to an integer to fix the problem.

```python
a = 5
b = "3"
print(a + int(b))
```

{try it}(python3 code/operators/playground-type-cast.py 4)

Data read from the keyboard or a file is always stored as a string. If you want to use this data, you will need to know how to convert it to the proper data type.

{Check It!|assessment}(multiple-choice-3899963352)
