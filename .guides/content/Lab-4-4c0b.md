## Count the Vowels
You are going to write a program that counts the number of vowels that appear in a string. For the purpose of this exercise, vowels are `a, e, i, o, u`.

### Variables
For this project, you will need three variables. One will be the string. Another will be a string of all the vowels (`"aeiou"`). The final variable will be a count of all the vowels.

```python
my_string = "The Brown Dog Jumps Over The Lazy Fox"
vowels = "aeiou"
count = 0
```

### String Iteration
A simple for loop will check each character in the string.

```python
for char in my_string:
```

### Checking for a Vowel
You could have a long set of conditionals that ask if `char` is `a`, then ask if it is `e`, etc. Since the vowels are represented as a string, much more efficient way to do the same thing is to ask if `char` is one of the characters in `vowels`. This is done with the `in` operator.

```python
    if char in vowels:
```

There is one problem with the line of code above. The string `vowels` is a string of lowercase characters. If `char` is an uppercase character, the conditional would return `False`. The easiest way to solve this issue is convert `char` to lowercase.

```python
    if char.lower() in vowels:
```

### Incrementing the Counter
When `char` is found in the string of vowels, increment the `count` variable.

```python
        count += 1
```

### Printing the Result
The last step is to print the result. Use the `format` method to provide some context. It is possible that a string could have only one vowel. The text you print should be grammatically correct. Use a conditional to determine if there is one vowel. Use the appropriate grammar if true, or use a different sentence if there are more than one vowel. Having zero values would use the same syntax as many vowels.

```python
if count == 1:
    print("There is 1 vowel in the string")
else:
    print("There are {} vowels in the string".format(count))
```

{try it}(python3 code/strings/lab4.py)

You should see that there are 9 vowels in the string.

<details><summary>**Code**</summary><img src=".guides/images/count-vowels.png" /></details>

{Check It!|assessment}(multiple-choice-887107274)
