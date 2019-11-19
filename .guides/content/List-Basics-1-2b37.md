----------

## What is a List?

Lists are a built-in data structure that groups information together. Lists do not have to be of the same data type, but often are. Lists are declared with the `[]` brackets, and a comma separates each item in a list. Lists are mutable, which means you can alter them in a variety of ways.

```python
int_list = [1, 2, 3, 4, 5]
string_list = ["John", "Paul", "George", "Ringo"]
mixed_list = [0.87, "hello", True, 17]

print(int_list)
print(string_list)
print(mixed_list)
```

{try it}(python3 code/lists/list-basics.py 1)

|||challenge
## What happens if you:
* Remove the commas from a list?
* Remove the quotes from around `"hello"`?
* Declare a variable `hello` and assign it the value `"hi"` (`hello = "hi"`)?

|||

{try it}(python3 code/lists/list-basics.py 2)

## Populating a List

You can use the `range` function to create a sequence of numbers for a list. The syntax is slightly different from a for loop. There is an extra `i` before the for loop.

```python
my_list = [i for i in range(1, 51)]

print(my_list)
```

{try it}(python3 code/lists/list-basics.py 3)

`my_list` is composed of the variable `i`, which is defined by all numbers from 1 up to but not including 51 (so all integers from 1 to 50).

|||challenge
## What happens if you:
* Change the range to `range(50)`?
* Change the range to `range(0, 50, 2)`?
* Change the range to `range(50, 0, -1)`?

|||

{try it}(python3 code/lists/list-basics.py 4)

<details><summary>**The Empty List**</summary>There is a special list called an empty list. This is a list that has no elements. An empty list looks like this: `my_list = []`. We will see how to add elements to an empty list in a later lesson.</details>

{Check It!|assessment}(multiple-choice-3464309383)

