----------

## Comparing with ==

The `==` operator can be used with strings just like it is with numbers or boolean values.

```python
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 == string2)
```

{try it}(python3 code/strings/boolean-comparison.py 1)

|||challenge
## What happens if you:
* Change the value of `string1` to `"it's friday!"`?
* Change the value of `string2` to `"it\'s friday!"`?

|||

{try it}(python3 code/strings/boolean-comparison.py 2)

## Comparing with !=

You can also test for string inequality with the `!=` operator.

```python
string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 != string2)
```

{try it}(python3 code/strings/boolean-comparison.py 3)

|||challenge
## What happens if you:
* Change the value of `string2` to `"It's Friday"`?
* Change the value of `string2` to `"It's Friday!"`?

|||

{try it}(python3 code/strings/boolean-comparison.py 4)

{Check It!|assessment}(fill-in-the-blanks-1789216035)
