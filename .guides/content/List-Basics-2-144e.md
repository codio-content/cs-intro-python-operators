----------

## List and its Index

Each piece of data in a list is called an element. You can access elements of a list with an index, which is like an address for each element. Start counting with index 0. The first element in the image below would be `my_list[0]`.

![List Indices](.guides/images/list-and-index.png)

```python
my_list = [5, 10, 15, 20]

print(my_list[0])
```

{try it}(python3 code/lists/list-basics-2.py 1)

|||challenge
## What happens if you:
* Change the index to 2 (`print(my_list[2]`)?
* Change the index to 4 (`print(my_list[4]`)?
* Change the index to 2 (`print(my_list[-1]`)?
* Change the index to 1.5 (`print(my_list[1.5]`)?

|||

{try it}(python3 code/lists/list-basics-2.py 2) 

<details><summary>**Negative Indecies**</summary>Python allows you to use a negative number as an index. `-1` is the last element of the list, `-2` is the second to last, etc. It is possible to generate an error message with a negative index. Try the code above with `-5` as the index.</details>

## Modifying a List

You can use the assignment operator (`=`) to change the value of an element. Be sure the reference the element with the appropriate index.

```python
my_list = [1, 2, 3]
print(my_list)

my_list[0] = 4
my_list[1] = 5
my_list[2] = 6
print(my_list)
```

{try it}(python3 code/lists/list-basics-2.py 3)

|||challenge
## What happens if you:
* Change an assignment to be `my_list[0] = "hello"`?
* Change an assignment to be `my_list[0] = 5 % 2 > 0`?
* Change an assignment to be `my_list[0] = my_list[2]`?

|||

{try it}(python3 code/lists/list-basics-2.py 4)

{Check It!|assessment}(fill-in-the-blanks-2442920593)

