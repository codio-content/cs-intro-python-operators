----------



<details><summary>**Raw Text**</summary>When writing to text files, Python outputs raw text. Raw text is the text that appears in a text editor. There is no special formatting or extra information attached to this text. Text in MS Word is not raw text. Raw text files have the extension `.txt`.</details>

Run the code and look in the directory tree. What do you see? When Python tries to open a file that does not exist, it creates the file.

## Writing to a File

Once the file is opened, the `writelines()` method is used to write text to the file. Any string of text passed to `writelines()` will appear in the file. Once you are done writing to the file, close the file.

```python
import os

path = "student_folder/text"

output_file = open(os.path.join(path, "practice1.txt"), "w")
output_file.writelines("Hello there")
output_file.close()
```

{try it}(python3 code/files/writing.py 2)
[Open File](open_preview student_folder/text/practice1.txt)

Run the code and click on `practice1.txt`. The text `Hello there` should be in the file.

|||challenge
## What happens if you:
* Change the string in `writelines()` to `"Goodbye"`?
* Change the string in `writelines()` to `""`?
* Change the mode to `open("practice1.txt", "r")`?

|||

{try it}(python3 code/files/writing.py 3)
[Open File](open_preview student_folder/text/practice1.txt)

{Check It!|assessment}(multiple-choice-1199134570)
