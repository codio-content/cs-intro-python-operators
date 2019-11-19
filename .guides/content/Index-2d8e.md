## The Index Method

The `index` method returns the element at a given index of a list. `index` has one parameter, an integer that is an index of the list.

![Index Method](.guides/images/list-index-method.png)

```python
my_list = ["dog", True, 16, "house", 55.9, False, 0]
element = my_list.index(3)
print(element)
```

{try it}(python3 code/lists/list-index.py 1)

|||challenge
## What happens if you:
* Change the value of `element` to `my_list.index(1)`?
* Change the value of `element` to `my_list.index(-1)`?
* Change the value of `element` to `my_list.index(len(my_list))`?

|||

{try it}(python3 code/lists/list-index.py 2)

{Check It!|assessment}(fill-in-the-blanks-3349955060)

