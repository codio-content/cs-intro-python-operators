----------

## Iterating Over Lists

The previous topics about lists have been about dealing with the list as a whole (sort, reverse, etc.) or dealing with individual elements of the list (pop, max, etc.). Iterating over a list allows you to deal with all of the elements in a list individually. Iterating over the list means to start with the element at index 0, and then progress until you reach the end of the list. A for loop is used to iterate over a list.

![Iteration Variable](.guides/images/iterating-list-variable-name.png)

<details><summary>**Number & Numbers**</summary>In the example below, the iteration variable is `number` and the list is named `numbers`. This is a very common practice in Python. The list is always plural, while the iterating variable is the singular of the list name. Python will not throw an error if this convention is not followed. However, `for number in numbers` helps with the readability of your code. You should follow this convention as often as possible.</details>

```python
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
```

{try it}(python3 code/lists/list-iterate.py 1)

|||challenge
## What happens if you:
* Change the value of `numbers` to `[101, 12, 36, 24, 55, 6]`?
* Change the value of `numbers` to `["cat", "dog", "mouse", "bird", "fish"]`?
* Change the `print` statement to `print(numbers)`?

|||

{try it}(python3 code/lists/list-iterate.py 2)

## What Happens Behind the Scene

Use the code visualizer below and step through the code. Notice how the variable `number` is the value of the element. The index of the list is never referenced.

<iframe width="700" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=numbers%20%3D%20%5B1,%202,%203,%204%5D%0Afor%20number%20in%20numbers%3A%0A%20%20%20%20print%28number%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


{Check It!|assessment}(fill-in-the-blanks-4088401606)

