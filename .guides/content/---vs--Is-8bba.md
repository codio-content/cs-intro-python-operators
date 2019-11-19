----------

## Why Have Is and ==?

It may seem like `is` and `==` do the same thing, but there is a subtle difference between the two. Enter and run the code below.

```python
a = 1
b = 1
print(id(a))
print(id(b))
```

{try it}(python3 code/strings/why-is.py 1)

You should see two identical numbers. These numbers are the object ID for the values stored in variables `a` and `b` (the `id` command returns the object ID). Each time you create a variable, Python takes some of the memory on your computer and reserves it for the variable. The more memory that is taken up by Python, the slower your program runs. Python increases performance by having two variables with the same value point to the same object in memory. Change your code to the following:

```python
a = 1
b = 1
print(id(a))
print(id(b))
a += 1
print(id(a))
print(id(b))
```
{try it}(python3 code/strings/why-is.py 2)

Because the variable `a` has a different value, Python cannot use the same object ID. A new chunk of memory is used, which is why the object IDs are different.

## Is and Object IDs

The `is` keyword compares object IDs, while `==` compares values. You should use `is` to compare strings and other objects (more on objects in another unit), and use `==` to compare floats and integers. The code below works, the `print` statements both return `True`. You will not get an error if you use `==` to compare strings. However, it is a good idea to get into the habit of use `is` for comparing strings and other objects.

```python
string1 = "Hello"
string2 = "Hello"
print(string1 == string2)
print(string1 is string2)
```
{try it}(python3 code/strings/why-is.py 3)

{Check It!|assessment}(multiple-choice-3362327903)
