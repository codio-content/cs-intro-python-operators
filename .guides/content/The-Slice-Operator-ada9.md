## The Slice Operator

The slice operator (`:`) returns a portion of the list. Provide numbers around the slice operator to indicate where you start and stop. The slice operator includes the first number, but does **not include** the second number. The slice operator does not modify the original list. Instead, it returns a portion of the list.

![List Slice](.guides/images/list-slice.png)

```python
my_list = ["red", "orange", "yellow", "green"]
my_slice = my_list[0:2]

print(my_slice)
```

{try it}(python3 code/lists/list-slice.py 5)

|||challenge
## What happens if you:
* Change the slice to be `my_list[1:2]`?
* Change the slice to be `my_list[0:len(my_list)]`?
* Change the slice to be `my_list[1:1]`?
* Change the slice to be `my_list[:2]`?

|||

{try it}(python3 code/lists/list-slice.py 6)

<details><summary>**Slice Defaults**</summary>If no number is used for the starting point in a slice `my_list[:2]`, Python will default to 0. If no number is used for the stopping point `my_list[2:]`, Python will default to the end of the list. Using no numbers on a slice `my_list[:]`, Python will default to 0 for the start and the end of the list as the stopping point. In short, Python will return the entire list.</details>

{Check It!|assessment}(parsons-puzzle-2278057412)
