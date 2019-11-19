## Reverse a String

You are going to write a program that takes a string and prints it in reverse order.

### Variables
You are going to need two variables. The first is the original string. Since strings are immutable, we will need a second variable to represent the reversed string. Make the reversed string an empty string.

```python
my_string = "The brown dog jumps over the lazy fox"
reversed_string = ""
```

Since the string needs to be reversed, our loop should start at the end of the string and work its way to the first character. So the for loop used in Lab 1 will not work. We are going to use a while loop. To do this, we need a variable that represents the index. Normally, the index starts at zero, but this loop will go backwards through the string. The starting index needs to be the last character in the string. The `length` method returns the length of a string. However, the length of a string is always one greater than the last index (because indexes start counting at zero). So the starting index should be the length of the string minus one.

```python
index = len(my_string) - 1
```

### String Iteration
The while loop should run as long as `index` is greater or equal to 0.

```python
while index >= 0:
```

Reversing a string comes down to taking the a character from the end and putting it at the front of a new string. This will be done by appending the character at `index` to `reversed_string`. It is important to remember that strings are immutable. The line of code below is overwriting `reversed_string` with a new string. It is not updating the contents of the string.

```python
    reversed_string += my_string[index]
```

Decrement the `index` variable to avoid an infinite loop.

```python
    index -= 1
```

### Printing the result
Once the loop has finished running, print `reversed_string`.

```python
print(reversed_string)
```

You should see `xof yzal eht revo spmuj god nworb ehT`.

{try it}(python3 code/strings/lab2.py)

<details><summary>**Code**</summary><img src=".guides/images/reverse-string.png" /></details>

{Check It!|assessment}(multiple-choice-1456526025)
