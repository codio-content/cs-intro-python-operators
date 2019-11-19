----------

## The Pop Method

There are some list methods that do not require parameters. You still must use the parentheses even if there are no parameters. The `pop` method is an example of this. The `pop` method removes and returns the last element of a list.

![List Method with No Parameters](.guides/images/list-method-no-parameters.png)

**Translation:** Pop (remove and return) the last element from the list `my_list`.

```python
my_list = [1, 2, 3, 4]
print(my_list)
print(my_list.pop())
print(my_list)
```

{try it}(python3 code/lists/list-pop.py 1)

|||challenge
## What happens if you:
* Change the code to:
```python
my_list = [1, 2, 3, 4]
print(my_list)
my_list.pop()
my_list.pop()
my_list.pop()
my_list.pop()
print(my_list)
```
* Add one more `my_list.pop()` before the `print` statement?

|||

{try it}(python3 code/lists/list-pop.py 2)

<details><summary>**`pop` versus `my_list[-1]`**</summary>`my_list[-1]` returns the last element in a list. This **does not** modify the original list. The `pop` method also returns the last element of a list, but it **always** modifies the original list. The last element has been removed from the list.</details>

## Optional Parameters

The `pop` method has optional parameters. That means if you do not put anything between the parentheses, it will pop off the last element (index of -1) in the list. If you want to remove a different element, put the element's index between the parentheses.

![Optional Parameters](.guides/images/optional-parameters.png)

```python
my_list = [1, 2, 3, 4]
delete = 0
print(my_list.pop(delete))
print(my_list)
```

{try it}(python3 code/lists/list-pop.py 3)

|||challenge
## What happens if you:
* Change `delete` to `delete = 2`?
* Change `delete` to `delete = -1`?
* Change `delete` to `delete = 4`?

|||

{try it}(python3 code/lists/list-pop.py 4)

{Check It!|assessment}(parsons-puzzle-2033383199)
