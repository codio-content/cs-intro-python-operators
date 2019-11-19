## The Count Method

The `count` method will count how many times an element appears in a list. `count` has one parameter, the element you wish to count.

```python
my_var = 2
my_list = [2, "red", 2.0, my_var, "Red", 8 // 4]
print(my_list.count(2))
```

{try it}(python3 code/lists/list-count.py 1)

|||challenge
## What happens if you:
* Change `2.0` to `2.00000001`?
* Change the `print` statement to `print(my_list.count("red"))`?
* Change the `print` statement to `print(my_list.count(99))`?

|||

{try it}(python3 code/lists/list-count.py 2)

{Check It!|assessment}(parsons-puzzle-3051307281)

