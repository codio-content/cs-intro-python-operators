----------

## Iterating Over Strings

You have seen how you can make a copy of individual characters in a string with their index. Iterating over a string allows you to deal with each character of a string individually. You start with the character at index 0 and move through the end of the string.

![String Iteration](.guides/images/iterating-string-variable-name.png)

```python
my_string = "Hello world"
for char in my_string:
    print(char)
```

{try it}(python3 code/strings/string-for-loop.py 1)

|||challenge
## What happens if you:
* Change the value of `my_string` to `"10, 11, 12, 13, 14"`?
* Change the value of `my_string` to `"\u25A3\u25A8\u25D3\u25CC\u25A2"`?
* Change the `print` statement to `print(my_string)`?

|||

{try it}(python3 code/strings/string-for-loop.py 2)

## Behind the Scenes

Use the code visualizer below and step through the code. Notice how the variable `char` is the value of the character. The index of the string is never referenced.

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=my_string%20%3D%20%22Hello%20world%22%0Afor%20char%20in%20my_string%3A%0A%20%20%20%20print%28char%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

{Check It!|assessment}(fill-in-the-blanks-1938628481)

