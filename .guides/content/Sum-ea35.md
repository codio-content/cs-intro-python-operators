----------

## The Sum Function

The next few lessons will be focused on functions that work with lists of numbers. Using a function or a method on a list is similar in that an action performed on the list. The syntax for calling a function is different than calling a method.

![List Functions and Methods](.guides/images/list-functions-methods.png)

The `sum` function is a built-in function that calculates the sum of a list.

```python
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(total)
```

{try it}(python3 code/lists/list-sum.py 1)

|||challenge
## What happens if you:
* Change the value of `my_list` to `[-45, 21, 6, 0.3]`?
* Change the value of `my_list` to `[]`?

|||

{try it}(python3 code/lists/list-sum.py 2)

## The Sum Function & Strings

You can concatenate strings with the `+` operator, which the same operator used to add numbers. This may seem like it is possible to use the `sum` function with a list of strings. However, this will cause an error message.

```python
my_list = ["abc", "def", "ghi"]
print(sum(my_list))
```

{try it}(python3 code/lists/list-sum.py 3)

|||challenge
## What happens if you:
* Change the value of `my_list` to `[1, 2, 3, "red"]`?

|||

{try it}(python3 code/lists/list-sum.py 4)

{Check It!|assessment}(parsons-puzzle-3133020826)

