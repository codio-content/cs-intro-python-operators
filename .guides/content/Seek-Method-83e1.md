----------

## Seek Method

The seek method takes an integer as a parameter, and causes Python to go to a specific character in the text file. The integer is the index for the text file. So `seek(0)` is the first character of the file, `seek(1)` is the second character, etc.

```python
import os

path = "student_folder/text"

with open(os.path.join(path, "read_practice.txt"), "r") as read_file:
    read_file.seek(30)
    print(read_file.readline())
    read_file.seek(0)
    print(read_file.readline())

```

{try it}(python3 code/files/seek.py 1)

|||challenge
## What happens if you:
* Change a `seek` to `180`?
* Change a `seek` to `1000`?
* Change a `seek` to `-1`?

|||

{try it}(python3 code/files/seek.py 2)

## Read a File Multiple Times

It was previously stated that a file cannot be read multiple times. That is true when trying to use `readlines` twice. You must close and then open the file to read it again. However, the `seek` method can also be used to move Python back to the beginning of the text file.

```python
import os

path = "student_folder/text"

with open(os.path.join(path, "read_practice.txt"), "r") as read_file:
    print("First Time")
    for line in read_file.readlines():
        print(line, end="")
    read_file.seek(0)
    print("\n\nSecond Time")
    for line in read_file.readlines():
        print(line, end="")
```

{try it}(python3 code/files/seek.py 3)

{Check It!|assessment}(multiple-choice-1830585668)
