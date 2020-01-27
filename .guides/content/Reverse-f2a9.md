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

<details><summary>**Reverse Sort**</summary>The `reverse` function may not perform a reverse sort of a list, but that does not mean it cannot be done. First, make sure that your list works with the `sort` method. A list of strings and numbers cannot be sorted. Next, sort the list with the `sort` method. Finally, use the `reverse` method to reverse the list's order. You should have a list in descending order. </details>

{try it}(python3 code/lists/list-reverse.py 2)

{Check It!|assessment}(multiple-choice-2506931680)