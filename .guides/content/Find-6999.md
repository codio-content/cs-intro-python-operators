----------

## The Find Method

The `find` method searches for a word or character in a string. If the word or character is found, the index is returned. If not, `-1` is returned. You can tell `find` where to start the search and where to end the search. By default, `find` will search the entire string.

![Find Method](.guides/images/find-method.png)

```python
string1 = "The brown dog jumps over the lazy fox."
string2 = "brown"
print(string1.find(string2))
```

{try it}(python3 code/strings/find-method.py 1)

|||challenge
## What happens if you:
* Change `string2` to `"zebra"`?
* Change `string2` back to `"brown"` and change the `print` statement to `print(string1.find(string2, 10))`?
* Change the `print` statement to `print(string1.find(string2, 0, 3))`?

|||

{try it}(python3 code/strings/find-method.py 2)

{Check It!|assessment}(parsons-puzzle-4291022967)

