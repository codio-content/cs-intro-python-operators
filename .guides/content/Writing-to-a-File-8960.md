----------

## Locating Student Files

In this unit, you will see a directory tree on the left. Notice, there is no such file called `practice1.txt`. This file does not exist.

<details><summary>**Raw Text**</summary>When writing to text files, Python outputs raw text. Raw text is the text that appears in a text editor. There is no special formatting or extra information attached to this text. Text in MS Word is not raw text. Raw text files have the extension `.txt`.</details>

You need a variable to represent the file, so create a variable named `output_file`. The first thing to do when working with a file is to use the `open` command to open a file and select the mode. There are three modes: write, append, and read. The code below will open a file called `practice1.txt` in write mode.

![Open File](.guides/images/open-file.png)

```python
output_file = open("practice1.txt", "w")
```

{try it}(python3 code/files/writing.py 1)

Run the code and look in the directory tree. What do you see? When Python tries to open a file that does not exist, it creates the file.


## Writing to a File

Once the file is opened, the `writelines()` method is used to write text to the file. Any string of text passed to `writelines()` will appear in the file. Once you are done writing to the file, close the file.

```python
output_file = open("practice1.txt", "w")
output_file.writelines("Hello there")
output_file.close()
```

{try it}(python3 code/files/writing.py 2)

Run the code and click on `practice1.txt`. The text `Hello there` should be in the file.

|||challenge
## What happens if you:
* Change the string in `writelines()` to `"Goodbye"`?
* Change the string in `writelines()` to `""`?
* Change the mode to `open("practice1.txt", "r")`?

|||

{try it}(python3 code/files/writing.py 3)

{Check It!|assessment}(multiple-choice-1199134570)
