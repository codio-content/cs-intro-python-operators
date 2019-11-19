----------

## User Input

To humans, the words "dog" and "Dog" are the same. Python, however, is case sensitive. That means a difference in capitalization implies two different words. When dealing with user input, the rules of capitalization are often not followed. The `input` command instructs Python to pause the program until the user has typed something and pressed `Return`. **Important**, Python treats all user input as a string. If you want a number, use typcasting to convert it to the proper data type.

![User Input](.guides/images/user-input.png)

<details><summary>**The Terminal**</summary>Collecting user input requires the terminal (also called the command line), which has not been used up until now. When you run the program below, you will see a new tab appear with the message to the user. Enter some text and press return. Click the "TRY IT" button to run the program again. If you want to edit your program, you can click on the tab with your code. You can also close the terminal (running the program again will launch the terminal).</details>

```python
text = input("Type something and press 'Return': ")
print(text)
```

{try it|terminal}(python3 code/strings/capitalization-comparison.py)

|||challenge
## What happens if you:
* Remove the space between the `:` and `"` in the `input` message?
* Press the `Ctrl` button and `C`?

|||

{try it|terminal}(python3 code/strings/capitalization-comparison.py)

<details><summary>**Ctrl + C**</summary>Pressing `Ctrl` and `C` on the keyboard will exit the program running in the terminal.</details>

## Comparing Text, Not Capitalization

You can compare the strings while ignoring capitalization by using the `lower` method. This will make all of the text lowercase. Make sure that both strings are lowercase for the comparison to work. 

```python
print("This program will check to see if two values are the same.")
string1 = input("Enter a value: ").lower()
string2 = input("Enter another value: ").lower()
if string1 is string2:
    print("They are the same!")
else:
    print("They are not the same.")
```

{try it|terminal}(python3 code/strings/capitalization-comparison.py)

|||challenge
## What happens if you:
* Enter `Texas` and `texas`?
* Enter `TeXaS` and `tExAs`?
* Change the `.lower()` to `.upper()` for both string variables?

|||

{try it|terminal}(python3 code/strings/capitalization-comparison.py)

<details><summary>**Running Python code manually**</summary>All the "TRY IT" button does is send a message to Codio to run your Python program. You can do the same from the terminal. The image below explains how to run your code manually. If you see the `$` in the terminal, that means Python has finished running, and the terminal is waiting for the next command. You can access the terminal by click the "Tools" menu and then select "Terminal".<img src=".guides/images/run-code-terminal.png" /></details>

{Check It!|assessment}(multiple-choice-3617041259)

