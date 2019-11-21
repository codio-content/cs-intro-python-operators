## Locating Student Files

In this unit, you will see a directory tree on the left. Inside `student_folder` are two more folders, `csv` and `text`. You will need to know how to access these folders and subfolders with Python code. The location of a file is called its path. You will be working with text files first. So the path for all of these activities is the `text` folder, which inside another folder called `student_folder`. Inside `text` is a file called `practice1.txt`. This is the file you want to access.

![File Path](.guides/images/file-path.png)

The path is `students_folder/text`. You will need to import the `os` module to use a path. This allows Python to interact with the operating system. Also, declare a variable `path` and assign it the string value of the path. Python requires a variable that represents the opened text file. Declare the variable `output_file`. Assign it the value of `practice1.txt`. Python needs the name and path of the file to open. This is where the `os` module comes in; `os.path.join(path, "practice1.txt)` is the command that joins `student_folder/text` and `practice1.txt` together. Now that you have the path and file name, you can open the file with the `open` command. The `open` command has three different modes: read, write, and append. Open the file in write mode.

![Open File](.guides/images/open-file.png)

```python
import os

path = "student_folder/text"

output_file = open(os.path.join(path, "practice1.txt"), "w")
```

{try it}(python3 code/files/writing.py 1)
[Open File](open_preview student_folder/text/practice1.txt)