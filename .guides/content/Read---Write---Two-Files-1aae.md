----------

## Read from One File and Write to Another

It is possible to open a file in read mode and another in write mode. Information can be passed from the reading file to the writing file. Like previous examples, `with open` will be used to open both files at once. The code below will open the file `read_practice` in read mode, create `destination.txt` in write mode, read the lines from the source file, and write these lines to the destination file. 

```python
import os

path = "student_folder/text"

with open(os.path.join(path, "read_practice.txt"), "r") as source, open(os.path.join(path, "destination.txt"), "w") as dest:
    for line in source.readlines():
        dest.write(line)
```

<details><summary>**`write` vs `writelines`**</summary>In the code above the `write` method is being used to write text to a file. Previously, the method `writelines` was used to write text to a file. What's the difference? `writelines` can accept a single string or a list of strings as shown in previous lessons. `write`, however, can only accept a single string.</details>

{try it}(python3 code/files/read-write-two-files.py 1)
[Open destination.txt](open_preview destination.txt)

|||challenge
## What happens if you:
* Change the for loop to:
```python
for line in source.readlines():
    line.upper()
    dest.write(line)
```

* Change the for loop to:
```python
for line in source.readlines():
    line += "\n"
    dest.write(line)
```

|||

{try it}(python3 code/files/read-write-two-files.py 2)
[Open destination.txt](open_preview destination.txt)

{try it}(python3 code/path/to_file.py 4)

{Check It!|assessment}(fill-in-the-blanks-810907680)
