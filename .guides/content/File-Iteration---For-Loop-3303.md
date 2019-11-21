----------

## File Iteration - For Loop

The `readlines` method returns all of the text at once. A loop allows you to deal with each line individually. To print out the text as it would normally appear, use a for loop to print each line of the text.

```python
import os

path = "student_folder/text"

with open(os.path.join(path, "read_practice.txt"), "r") as read_file:
    for line in read_file.readlines():
      print(line)
```

{try it}(python3 code/files/file-iteration.py 1)

<details><summary>**Reading a file multiple times**</summary>When Python reaches the end of a file with `readlines`, it will not start back at the beginning until you close the file and then reopen it.</details>

|||challenge
## What happens if you:
* Change the print statement to `print(line.upper())`?
* Change the print statement to `print(line.replace("a", "\U0001F61C")))`?

|||

{try it}(python3 code/files/file-iteration.py 2)

## Extra Lines

You probably noticed that the printed text has an empty line between lines of text. If you open the original text file, there are no empty lines. The orignal text has a newline character at the end of each line. The print command also adds a newline character by default. So Python prints two new lines: the first one goes to the next line, the second one creates the blank line. Use `end=""` in the print statement to remove the blank line. This replaces the newline character with an empty string.

```python
import os

path = "student_folder/text"

with open(os.path.join(path, "read_practice.txt"), "r") as read_file:
    for line in read_file.readlines():
      print(line, end="")
```

{try it}(python3 code/files/file-iteration.py 3)

|||challenge
## What happens if you:
* Change the print statement to `print(line, end="!")`?
* Change the print statement to `print(line, end="\n\n\n")`?

|||

{try it}(python3 code/files/file-iteration.py 4)

{Check It!|assessment}(multiple-choice-2796587801)