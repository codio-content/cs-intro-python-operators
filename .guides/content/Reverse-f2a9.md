## The Reverse Method

The `reverse` method reverses the order of a list. `reverse` **is not** a reverse sort. It does not have a parameter. The `reverse` method does not return a new list, it modifies the original list.

![Reverse Method](.guides/images/list-reverse.png)

```python
my_list = ["north", True, 45, 12, "red"]
print(my_list)
my_list.reverse()
print(my_list)
```

{try it}(python3 code/lists/list-reverse.py 1)

|||challenge
## What happens if you:
* Change the list to `my_list = [1, 4, 6, 2, 7, 3, 5]`?
* Change the list to `my_list = [1]`?

|||

{try it}(python3 code/lists/list-reverse.py 2)

{Check It!|assessment}(multiple-choice-2506931680)