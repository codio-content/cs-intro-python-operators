## Locating Student Files

This unit is all about working with files on a computer. The firs step is to open the desired file. That means navigating the file system to find the file in question. The open command requires the location (path) of the file and the filename. The file is called `practice1.txt`. It is located in the `text` folder, which is inside the folder called `student_folder`.  **This makes the path `student_folder/text/`.**

![File Path](.guides/images/file-path.png)

Importing the `os` Python module allows Python to interact with the operating system. `os` can also join the file path and filename together, allowing you to open the file. 

![Open File](.guides/images/open-file.png)

There are three different modes when opening a file: read, write, and append. 

<details><summary>**Modes**</summary>The three different modes will be covered of the course of this unit. Use `"w"` to indicate the write mode, `"a"` to indicate the append mode, and `"r"` to indicate the read mode.</details>

Use the write mode. You most close files after you have finished working with them.

```python
import os

path = "student_folder/text"

output_file = open(os.path.join(path, "practice1.txt"), "w")
output_file.close()
``` 

{try it}(python3 code/files/writing.py 1)

<details><summary>**Where is the output?**</summary>You should see a green check mark after running your program. This means the code ran without any errors. But what about the output? The code above only opens and then closes a file.

|||challenge
## What happens if you:
* Open `student_folder` in the sidebar on the left. Open the `text` folder and right-click on `practice1.txt`. Select "Delete..." and run the program again.

|||

{Check It!|assessment}(multiple-choice-4246621000)
