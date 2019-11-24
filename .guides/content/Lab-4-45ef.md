----------

## Lab 4

The lab will cover how to encrypt the contents of a file with a Caesar cipher. This cipher will work with any characters that are letters (uppercase and lowercase), the digits 0 to 9, and the symbols space, exclamation, question mark, and the period. Other symbols will not be encrypted. The Caesar cipher requires a key to work as well. The key is any number from 0 to 25.

The Caesar cipher works by having a list of all of the symbols that can be encrypted. Take the letter you want to encrypt and find its place in the list. Add the value of the key to the position to get the encrypted letter. If the new position is greater than the end of the list, keep counting from the beginning of the list. The example below assumes a key of 13, and shows that a `"K"` becomes `"X"` with the Caesar cipher.

![Caesar Cipher](.guides/images/caesar-cipher.png)

### Reading the Source File
This program will read from a file called `source.txt` with the path of `student_files/.labs`. The encrypted text will be written into a file called `encrypted.txt` with the path of `student_files/text`. Create path variables for the source path and the encrypted path. Then open both files, `source.txt` in read mode and `encrypted.txt` in write mode. Import the `os` module as well.

```python
import os

source_path = "student_folder/.labs"
encrypted_path = "student_folder/text"

with open(os.path.join(source_path, "source.txt"), "r") as source, open(os.path.join(encrypted_path, "encrypted.txt"), "w") as destination:   
```

Next, you need set the key (a number from 0 to 25), the cipher mode (encrypt or decrypt), the list of symbols and an empty string of the new characters (either encrypted or decrypted).

```python
    key = 13
    mode = "encrypt"
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    new_text = ""
```

<details><summary>**Why is `SYMBOLS` in all caps?**</summary>There is a type of variable called a constant. This variable should never change its value. The Python community represents constants by using all caps when writing the variable name.</details>

Read the first line from the `source` file. If it is not an empty string (the end of the text file), then you are going to loop through each character of the line.

```python
    line = source.readline()
    while line != "":
        for char in line:
```

### The Caesar Cipher
The Caesar cipher can only encrypt those characters that are in the `SYMBOLS` variable. Check to see if `char` is in `SYMBOLS` and then find its index if true. If the program is encrypting the text, add the value of the key to the index. If the program is decrypting the text, subtract the value of the key from the index.

```python
            if char in SYMBOLS:
                char_index = SYMBOLS.find(char)
                
                if mode == "encrypt":
                    new_index = char_index + key
                elif mode == "decrypt":
                    new_index = char_index - key
```

It is possible that `char_index` is less than 0 or greater than the length of `SYMBOLS`. These indexes will cause a problem. If `char_index` is negative, add it to the length of `SYMBOLS`. If `char_index` is greater than the length of `SYMBOLS`, subtract the length of `SYMBOLS`.

```python
                if new_index >= len(SYMBOLS):
                    new_index = new_index - len(SYMBOLS)
                elif new_index < 0:
                    new_index = new_index + len(SYMBOLS)
```

Now that the character has been transformed according to the key, add the character to `new_text`. Once the for loop has finished running, write the new text to `destination`. Finally, read the next line in `source.

```python
                new_text += SYMBOLS[new_index]
  
        destination.write(new_text)
        line = source.readline()
```

{try it}(python3 code/files/lab4.py 1)
[Open the encrypted file](open_file student_folder/text/encrypted.txt)

<details><summary>**Code**</summary><img src=".guides/images/encryption.png" /></details>

### Decrypting the File
To decrypt the file, a few changes need to be made to your code. First, create a decrypted path. 

```python
decrypted_path = "student_folder/text"
```

You need to update the files that you are opening. The source file should be the encrypted file, and the destination file will be the file `decrypted.txt`. 

```python
with open(os.path.join(encrypted_path, "encrypted.txt"), "r") as source, open(os.path.join(decrypted_path, "decrypted.txt"), "w") as destination:
```

Finally, change the mode of the cipher to `"decrypt"`.

```python
    mode = "decrypt"
```

Run the program and take a look at the output below.

{try it}(python3 code/files/lab4.py 2)
[Open the decrypted file](open_file student_folder/text/decrypted.txt)

<details><summary>**Source Text**</summary>The original text for this lab is the [opening paragraph](http://www.gutenberg.org/files/55/55-h/55-h.htm#chap01) from L. Frank Baum's *The Wizard of Oz*.</details>

{Check It!|assessment}(multiple-choice-3180548474)
