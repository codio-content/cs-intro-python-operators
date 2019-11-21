----------

## Reading a Non-Existing File

Read mode works much like write or append mode. Use a `"r"` when opening a file. Notice, there a file named `read_practice.txt`. Remove the underscore from the filename to see if a new file will be created like with the write and append modes.

```python
import os

path = "student_folder/text"

read_file = open(os.path.join(path, "readpractice.txt"), "r")
read_file.close()
```

{try it}(python3 code/files/read.py 1)

Read mode does not create a new file if the file does not exist. You can only read previously existing files. 

## Reading a File

Return the underscore to the filename so that it is `read_practice.txt`. Use a print statement to print the contents of the file to the screen.

```python
import os

path = "student_folder/text"

read_file = open(os.path.join(path, "read_practice.txt"), "r")
print(read_file)
read_file.close()
```

{try it}(python3 code/files/read.py 2)

Notice that Python does not print the contents of the text file. Instead it prints information about the file object (name, mode, and encoding). If you want to print the contents of a text file, use the `readlines` method.

<details><summary>**UTF-8**</summary>There are many characters that go beyond letters and numbers. For example, punctuation, accents, symbols, emojis, etc. There needs to be a way to use these characters in a way that everybody can understand. Encoding is an agreed upon method for representing these characters. UTF-8 is by far the most popular way to encode text today. If you want to know more, check out this <a href="http://kunststube.net/encoding/">article</a>.</details>

```python
import os

path = "student_folder/text"

read_file = open(os.path.join(path, "read_practice.txt"), "r")
print(read_file.readlines())
read_file.close()
```

{try it}(python3 code/files/read.py 3)

Notice how the text is a list of strings, and the newline character (`\n`) is a part of the output.

  
{Check It!|assessment}(multiple-choice-3882923409)
