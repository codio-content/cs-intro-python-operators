----------

## Multiline Strings

Imagine that you want to write the words `Hello` and `there` on separate lines of a file called `practice2.txt`. If the `print` statement writes each string on its own line, the `writelines` should too.

```python
output_file = open("practice2.txt", "w")
output_file.writelines("Hello")
output_file.writelines("there")
output_file.close()
```

<details><summary>**Closing a File**</summary>Closing the file is an important step in working with files. If you forget to close a file, some unpredictable actions may take place. For example, if you open a file with newly written text before closing the file, that text may not be in the file. Be sure that you close all of the files that you open.</details>

{try it}(python3 code/files/multiline-strings-write.py 1)
[Open practice1.txt](open_preview practice2.txt)

If you want to have text appear on a new line, then you need to use the newline character (`\n`).

|||challenge
## What happens if you:
* Change the `writelines()` code to:
```python
output_file.writelines("Hello\n")
output_file.writelines("there")
```
* Change the `writelines()` code to:
```python
output_file.writelines("Hello\nthere")
```

|||

{try it}(python3 code/files/multiline-strings-write.py 2)
[Open practice1.txt](open_preview practice2.txt)

## A List of Strings

It is possible to use a list of strings with the `writelines()` method. However, these strings will be written one after another with no space between. If you want spaces, be sure to add them. If you want text to appear on a newline, use `\n`.

```python
lines_to_write = ["First sentence.", "Second sentence.", "Third sentence."]
output_file = open("practice2.txt", "w")
output_file.writelines(lines_to_write)
output_file.close()
```

{try it}(python3 code/files/multiline-strings-write.py 3)
[Open practice1.txt](open_preview practice2.txt)

|||challenge
## What happens if you:
* Change `lines_to_write` to `["First sentence. ", "Second sentence. ", "Third sentence."]`?
* Change `lines_to_write` to `["First sentence.\n", "Second sentence.\n", "Third sentence."]`?

|||

{try it}(python3 code/files/multiline-strings-write.py 4)
[Open practice1.txt](open_preview practice2.txt)

{Check It!|assessment}(parsons-puzzle-1430141663)
