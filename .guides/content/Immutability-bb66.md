----------

## Immutability

You now know how to reference each character of a string. What do you think the code below will do?

```python
my_string = "House"
my_string[0] = "M"
print(my_string)
```

{try it}(python3 code/strings/immutability.py 1)

If you thought the code above would print `Mouse`, that would be a logical guess. However, you see an error. Strings are immutable. That means you cannot change their value.

## Yes, but...

The code below works just fine. Isn't this an example of changing the value of a string?

```python
my_string = "House"
my_string = "Mouse"
print(my_string)
```

{try it}(python3 code/strings/immutability.py 2)

Python is doing something very subtle behind the scenes. The first example on this page is about mutability. That is, changing just a part of a whole. The second example is about the assignment operator. Assignment replaces the entire value with a new value. So, you can replace an entire string (assignment), but you cannot change part of a string (mutability). That is why strings are considered to be immutable.

![Mutability vs Assignment](.guides/images/string-immutability.png)

{Check It!|assessment}(multiple-choice-2460911919)
