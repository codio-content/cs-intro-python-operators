----------

## Comparing with Is

Python uses the keyword `is` for comparison. It replaces `==`.

```python
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 is string2)
```

{try it}(python3 code/strings/is-comparison.py 1)

|||challenge
## What happens if you:
* Change `string1` and `string2` to the value `""`?
* Change `string1` to the value `" "`?

|||

{try it}(python3 code/strings/is-comparison.py 2)

## Comparing with Is Not

If `==` can be replaced with `is`, then `!=` can be replaced with `is not`.

```python
string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 is not string2)
```

{try it}(python3 code/strings/is-comparison.py 3)

|||challenge
## What happens if you:
* Change `string1` to `"\""` and change `string2` to `"""`?
* Change `string1` to `"\""` and change `string2` to `'"'`?

|||

{try it}(python3 code/strings/is-comparison.py 4)

<details><summary>**Why the EOF error?**</summary>The string `"\""` is actually a string that looks like this `"`. But if you put three double quotes in a row, that is starting a multiline string. Python expects another triple quote to end the multiline string. Python reached the end of the file (EOF) before finding the triple quote. That is why there is an error.</details>

{Check It!|assessment}(fill-in-the-blanks-124411320)