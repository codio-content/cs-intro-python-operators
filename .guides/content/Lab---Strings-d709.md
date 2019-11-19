## Tutorial Lab 2: Strings

You can use the `+` and `*` operators with strings, even though the result is not based on math. Using the `+` operator with strings is called concatenation.

Use the text editor open in the left pane, and enter the following code:

```python
string_1 = "hip "
string_2 = string_1 * 2
string_3 = "hoo"
string_4 = "ray!"
string_5 = string_3 + string_4
print(string_2, end='')
print(string_5)
```

{Try it}(python3 code/operators/lab-strings.py)

To see what is happening in these operations, click [here](open_tutor code/operators/lab-strings.py). Click on the `Forward >` button to see how the calculations progress step by step.
1) Assign the value `"hip "` to the variable `string_1`. Note the inclusion of a space after the word `hip`.
2) The variable `string_2` will have the value `"hip hip "` because `string_1 * 2` repeats the value of `string_1` two times.
3) Declare `string_3` and assign it the value `hoo`.
4) Declare `string_4` and assign it the value `ray!`.
5) Declare `string_5` and assign it the value of `string_3` combined with the value of `string_4` (`hooray!`).
6) Print the value of `string_2` (`hip hip `) and also remove the newline character.
7) Print the value of `string_5` (`hooray!`) to the end of `string_2`.

{Check It!|assessment}(multiple-choice-2141727151)
