----------

## What is a List Method?

Lists have special commands called methods (more on methods in a later lesson). Methods have a special syntax. First, start with a list (often a variable that represents a list). Add a period after the list. Finally, add the name of the method with any parameters. Parameters are values that the method will use.

![List Method with Parameters](.guides/images/list-method-parameters.png)

**Translation:** Append the string `Hi` to the list `my_list`.

## The Append Method

The `append` method adds an element to a list. `append` adds the element to the end of the list.

```python
my_list = [1, 2, 3]
new_element = 4

my_list.append(new_element)
print(my_list)
```

{try it}(python3 code/lists/list-append.py 1)

|||challenge
## What happens if you:
* Change the value of `new_element` to `"four"`?
* Change the value of `new_element` to `len(my_list)`?
* Change the value of `new_element` to `my_list[0]`?

|||

{try it}(python3 code/lists/list-append.py 2)

<details><summary>**`append` versus `+`**</summary>There is an important difference between `append` and the concatenation operator (`+`). The `+` operator only combines two lists.The `append` method can add a value of any data type to a list.</details>

{Check It!|assessment}(multiple-choice-1778093803)

