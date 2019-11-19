----------

## Variable Names
Variables are used to store a value, and these values have a data type. Data types describe the kind of information that is being stored. Numbers are different then text, and integers are different from numbers with decimals. Variable declaration is when you create a variable and assign it a value. Enter the name of the variable you want to create, a `=` (called the assignment operator), and the value you want to store in the variable. You do not have to indicate the data type when declaring a variable. Use the `print` statement to see the value of the variable.

```python
my_variable = "Hello world"
print(my_variable)
```

{try it}(python3 code/fundamentals/playground-variables1.py 1)

Do not use quotation marks when printing a variable. Using quotation marks will print the variable name, not its value.

```python
my_variable = "Hello world"
print(my_variable)
print("my_variable")
```

{try it}(python3 code/fundamentals/playground-variables1.py 2)

## Variable Naming Rules
Here are the rules for declaring a variable.

|Rule|Correct|Incorrect|
|----|-------|---------|
|Start with a letter or underscore|`variable`, `_variable`|`1variable`|
|Remainder of variable name is letters, numbers, or underscores|`var_i_able`, `var1able`|`var-i-able`, `var!able`|
|Cannot use a Python keyword|`my_class`|`class`|
|Variables are case sensitive|`variable`, `Variable`, and `VARIABLE` are all different variables|

<details><summary><b>What are the Python key words?</b></summary><table><tr><th></th><th></th><th></th><th></th></tr><tr><td>False</td><td>class</td><td>finally</td><td>is</td></tr><tr><td>return</td><td>None</td><td>continue</td><td>for</td></tr><tr><td>lambda</td><td>try</td><td>True</td><td>def</td></tr><tr><td>from</td><td>nonlocal</td><td>while</td><td>and</td></tr><tr><td>del</td><td>global</td><td>nont</td><td>with</td></tr><tr><td>as</td><td>elif</td><td>if</td><td>or</td></tr><tr><td>yield</td><td>assert</td><td>else</td><td>import</td></tr><tr><td>pass</td><td>break</td><td>except</td><td>in</td></tr><tr><td>raise</td></tr></table></details>

{Check It!|assessment}(multiple-choice-928839981)
