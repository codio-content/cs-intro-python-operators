----------

## The Title Method

The `title` method creates a copy of a string, and returns a string with the first letter of each word capitalized. All other characters of the word will be lowercase.

```python
my_string = "the big brown dog"
print(my_string.title())
```

{try it}(python3 code/strings/title-method.py 1)

|||challenge
## What happens if you:
* Change `my_string` to `"tHe BiG bRoWn DoG"`?
* Change `my_string` to `"thebigbrowndog"`?
* Change `my_string` to `"a1 1a a a a"`?

|||

{try it}(python3 code/strings/title-method.py 2)

<details><summary>**Other String Methods**</summary>There are [many more](https://www.tutorialspoint.com/python/python_strings.htm) string methods. Here are a few examples:<table><tr><th>Method</th><th>Example</th><th>Description</th></tr><tr><td>[Center](https://www.tutorialspoint.com/python/string_center.htm)</td><td>`center(width, fill)`</td><td>Center a string in a given width, fill any whitespace with a given character</td></tr><tr><td>[Count](https://www.tutorialspoint.com/python/string_count.htm)</td><td>`count(str, start, end)`</td><td>Count how many times a string appears</td></tr><tr><td>[Ends With](https://www.tutorialspoint.com/python/string_endswith.htm)</td><td>`endswith(str, start, end)`</td><td>Return `True` if a string ends with a specific string</td></tr><tr><td>[Index](https://www.tutorialspoint.com/python/string_index.htm)</td><td>`index(str, start, end)`</td><td>Return index of `str` in a string, will raise an exception if not found</td></tr><tr><td>[Is Alphanumeric](https://www.tutorialspoint.com/python/string_isalnum.htm)</td><td>`isalnum()`</td><td>Returns `True` if string is alphanumeric</td></tr><tr><td>[Is Alphabetic](https://www.tutorialspoint.com/python/string_isalpha.htm)</td><td>`isalpha()`</td><td>Returns `True` if string is alphabetic</td></tr><tr><td>[Is Digit](https://www.tutorialspoint.com/python/string_isdigit.htm)</td><td>`isdigit()`</td><td>Returns `True` if string is just digits</td></tr><tr><td>[Is Lower](https://www.tutorialspoint.com/python/string_islower.htm)</td><td>`islower()`</td><td>Returns `True` if the string is lowercase</td></tr><tr><td>[Is Space](https://www.tutorialspoint.com/python/string_isspace.htm)</td><td>`isspace()`</td><td>Returns `True` if the strings is nothing but spaces</td></tr><tr><td>[Is Title](https://www.tutorialspoint.com/python/string_istitle.htm)</td><td>`istitle()`</td><td>Returns `True` if the string is title case</td></tr><tr><td>[Is Upper](https://www.tutorialspoint.com/python/string_isupper.htm)</td><td>`isupper()`</td><td>Returns `True` if string is all uppercase</td></tr></table>

{Check It!|assessment}(multiple-choice-2695027968)
