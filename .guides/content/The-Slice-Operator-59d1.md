## The Slice Operator

The slice operator (`:`) returns a portion of the string. Provide numbers to the slice operator to indicate where you start and stop. The slice operator includes the first number, but does **not include** the second number. The slice operator does not modify the original string. Instead, it returns a partial copy of the original string.

![String Slice](.guides/images/string-slice.png)

```python
my_string = "The brown dog jumps over the lazy fox."
my_slice = my_string[4:9]

print(my_slice)
```

{try it}(python3 code/strings/string-slice.py 1)

|||challenge
## What happens if you:
* Change the slice to be `my_string[1:2]`?
* Change the slice to be `my_string[0:len(my_string)]`?
* Change the slice to be `my_string[1:1]`?
* Change the slice to be `my_string[:2]`?

|||

{try it}(python3 code/strings/string-slice.py 2)

<details><summary>**Slice Defaults**</summary>If no number is used for the starting point in a slice `my_string[:2]`, Python will default to 0. If no number is used for the stopping point `my_string[2:]`, Python will default to the end of the string. Using no numbers on a slice `my_string[:]`, Python will default to 0 for the start and the end of the string as the stopping point. In short, Python will return the entire string.</details>

{Check It!|assessment}(multiple-choice-2369717682)
