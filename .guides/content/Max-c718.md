----------

## The Max Function

The `max` function returns the largest element in a list.

```python
my_list = [50, 11, 0, 72, 102]
largest = max(my_list)
print(largest)
```

{try it}(python3 code/lists/list-max.py 1)

|||challenge
## What happens if you:
* Change the value of `my_list` to `[5 / 2, 5 // 2, 5 % 2]`?
* Change the value of `my_list` to `[1, 2, 3, 4, "5"]`?
* Change the value of `my_list` to `[]`?

|||

{try it}(python3 code/lists/list-max.py 2)

## The Max Function & Strings

If all of the elements of a list are strings, then the `max` function can be used to determine the element that would appear last in alphabetical order.

```python
my_list = ["house", "cat", "zebra", "dog", "bike"]
last = max(my_list)
print(last)
```

{try it}(python3 code/lists/list-max.py 3)

|||challenge
## What happens if you:
* Change the value of `my_list` to `["zzz", "zz", "zzzz", "z"]`?
* Change the value of `my_list` to `["one", "two", "three", "four"]`?
* Change the value of `my_list` to `["100", "27", "3000", "abc"]`?

|||

{try it}(python3 code/lists/list-max.py 4)

{Check It!|assessment}(multiple-choice-4085522795)

