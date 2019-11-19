----------

## Read from One File and Write to Another

It is possible to open a file in read mode and another in write mode. Information can be passed from the reading file to the writing file. Like previous examples, `with open` will be used to open both files at once. The code below will open the file `read_practice` in read mode, create `destination.txt` in write mode, read the lines from the source file, and write these lines to the destination file. 

```python
with open("read_practice.txt", "r") as source, open("destination.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)
```

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

## Topic 2

Short introduction

```python
Example code
```

{try it}(python3 code/path/to_file.py 3)

|||challenge
## What happens if you:
* Code suggestion
* Code suggestion

|||

{try it}(python3 code/path/to_file.py 4)

Insert reading question
