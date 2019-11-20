----------

## Append Mode

Write mode has some unusual behavior. Writing to a non-existent file creates the file. Writing to an already existing file erases the previous contents of the file. The append mode will also create a file if one does not already exist. However, append mode will not erase content already saved to the file. It will add the text to the end of the file. Run this code and look at the output.

```python
output_file = open("practice3.txt", "w")
output_file.writelines("First sentence")
output_file.close()
```

{try it}(python3 code/files/append.py 1)
[Open practice1.txt](open_preview practice3.txt)

Now append the following text to the file.

```python
output_file = open("practice3.txt", "a")
output_file.writelines("Second sentence")
output_file.close()
```

{try it}(python3 code/files/append.py 2)
[Open practice1.txt](open_preview practice3.txt)

|||challenge
## What happens if you:
* Change the append text to `writelines("\nSecond sentence")`?
* Change the program to:
```python
new_text = ["How many boards\n", "Could the Mongols hoard\n", "If the Mongols hordes got bored?"]
output_file = open("practice3.txt", "a")
output_file.writelines("new_text")
output_file.close()
```

|||

{try it}(python3 code/files/append.py 3)
[Open practice1.txt](open_preview practice3.txt)

## With Open

Opening and closing files is an important part of working with files, but it can be tedious to perform both steps. The `with open` command combines the two lines of code. Once the end of the indented code is reached, the file is automatically closed.

![With Open](.guides/images/with-open.png)

```python
with open("practice3.txt", "a") as output_file:
    output_file.writelines("Some new text!")
```

{try it}(python3 code/files/append.py 4)
[Open practice1.txt](open_preview practice3.txt)

|||challenge
## What happens if you:
* Change the text in `writelines()` to `"\nSome new text!"`?
* Change the program to:
```python
with open("practice3.txt", "a") as output_file:
    output_file.writelines("\nSome new text!")
    output_file.writelines("\nAnd some more text!")
    output_file.writelines("\nYet even more text!")
```

|||

{try it}(python3 code/files/append.py 5)
[Open practice1.txt](open_preview practice3.txt)

{Check It!|assessment}(fill-in-the-blanks-1777626410)
