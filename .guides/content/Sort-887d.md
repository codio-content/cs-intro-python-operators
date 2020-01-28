## The Sort Method

The `sort` method arranges a list in order. If the `sort` method does not have a parameter, then it will sort the list in ascending order. The `sort` method does not return a new list; instead it modifies the original list.

```python
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
print(my_list)
my_list.sort()
print(my_list)
```

{try it}(python3 code/lists/list-sort.py 1)

|||challenge
## What happens if you:
* Change the list to `my_list = ["zebra", "door", "apple", "cat", "deer", "bark"]`?
* Change the list to `my_list = [23, 15, "red", 90, -8, False]`?
* Change the list to `my_list = ["APPLE", "apple", "Apple"]`?

|||

{try it}(python3 code/lists/list-sort.py 2)

## Reverse Sort

The `sort` method has an optional parameter to sort a list in descending order. Use `reverse=True` as the parameter to reverse sort a list.

```python
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
```

{try it}(python3 code/lists/list-sort.py 3)

{Check It!|assessment}(multiple-choice-1411581104)

