----------

## List Length

Python has a function (`len`) to determine the length of a list. 

```python
list_1 = [12, 66, 52, 97, 28, 41, 7]
list_2 = [68, True, 34, False, 41.897, "apple"]

if len(list_1) > len(list_2):
    print("list_1 is longer than list_2")
elif len(list_1) == len(list_2):
    print("list_1 and list_2 are the same length")
else:
    print("list_2 is longer than list_1")
```

{try it}(python3 code/lists/list-length.py 1)

<details><summary>**The Empty List**</summary>We already talked about the empty list, `[]`. It is a list with no elements. You can define an empty list with code if `len(my_list) == 0` is true, then the list is an empty list.</details>

|||challenge
## What happens if you:
* Remove one of the elements from `list_1`?
* Add a few elements to `list_2`?
* Change `list_2` to `list_2 = [i for i in range(0, 20)]`?

|||

{try it}(python3 code/lists/list-length.py 2)

{Check It!|assessment}(multiple-choice-1182301890)

