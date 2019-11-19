----------

## String Length

We have already seen strings in the "Fundamentals"section. We are going to dig a little deeper with this data type. All strings have the following characteristics:

1) **Characters** - Strings are made up of characters between quotation marks (previously covered in the "Fundamentals" section).
2) **Length** - Each string has a length (total number of characters).
3) **Index** - Each character in a string has a position, called an index.

 To calculate the length of a string, use the `len` function. This function will return an integer that is the sum of all of the characters between the quotation marks.

```python
my_string = "Hello"
length = len(my_string)
print(length)
```

{try it}(python3 code/strings/string-properties.py 1)

|||challenge
## What happens if you:
* Change `my_string` to `"Hello world!"`?
* Change `my_string` to `""`?
* Change `my_string` to `"-1"`?

|||

{try it}(python3 code/strings/string-properties.py 2)

## String Index

Each character in a string has a position. This is its index. Indexes always start with 0.

![String Index](.guides/images/string-and-index.png)

<details><summary>**Strings & Quotation Marks**</summary>Quotation marks are required to declare the value of a string. However, quotation marks are not a part of the string itself. That is why quotation marks are not counted with the `len` function and why they do not have an index.</details>

To reference a character, use the string name, followed by square brackets (`[]`), and put the index between the square brackets.

![Referencing a Character with an Index](.guides/images/using-string-index.png)

```python
my_string = "Hello!"
character = my_string[1]
print(character)
```

{try it}(python3 code/strings/string-properties.py 3)

|||challenge
## What happens if you:
* Change `character` to `my_string[len(my_string)]`?
* Change `character` to `my_string[len(my_string) - 1]`?
* Change `character` to `my_string[-1]`?

|||

{try it}(python3 code/strings/string-properties.py 4)

{Check It!|assessment}(fill-in-the-blanks-2436923214)

