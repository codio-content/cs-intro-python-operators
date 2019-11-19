----------

## The Remove Method

The `remove` method has one parameter, the object to be removed from the list.

![List Remove](.guides/images/list-remove.png)

```python
my_list = [1, 2, 3, 3, 4]
my_list.remove(2)
print(my_list)
```

{try it}(python3 code/lists/list-remove.py 1)

|||challenge
## What happens if you:
* Change the `remove` method to `my_list.remove(3)`?
* Change the `remove` method to `my_list.remove(2 *2)`?
* Change the `remove` method to `my_list.remove(0)`

|||

{try it}(python3 code/lists/list-remove.py 2)

## Remove Versus Pop

What is the difference between the `remove` and `pop` methods? They both remove an element from a list, but there are some subtle differences as well.

|Pop|Remove|
|---|------|
|Removes an element|Removes an element|
|Removes based on index|Removes based on value|
|Returns the removed value|Does not return anything|

```python
list_1 = [1, 2, 3, 4, 5]
list_1.pop()
print(list_1)

list_2 = [1, 2, 3, 4, 5]
list_2.remove(5)
print(list_2)
```

{try it}(python3 code/lists/list-remove.py 3)

|||challenge
## What happens if you:
* Change the `pop` method to `list_1.pop(2)` and change the `remove` method to `list_2.remove(2)`?
* Change the code to be the following:
```python
list_1 = [1, 2, 3, 4, 5]
print(list_1.pop())

list_2 = [1, 2, 3, 4, 5]
print(list_2.remove(5))
```

|||

{try it}(python3 code/lists/list-remove.py 4)

{Check It!|assessment}(multiple-choice-4061005599)

