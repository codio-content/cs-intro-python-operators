## Tutorial Lab 2: Variables

Use the code editor to the left to enter the code below.

```python
string_variable = "This is a string"
float_variable = 3.14159
int_variable = 42
boolean_variable = True

string_variable = boolean_variable
float_variable = string_variable
int_variable = float_variable
boolean_variable = int_variable

print(int_variable)
```
Run the module to see the output. Use the code visualizer to go through the program step by step.

[Code Visualizer](open_tutor code/fundamentals/lab-variables.py)
{try it}(python3 code/fundamentals/lab-variables.py)

If you use the code visualizer, you will notice that all four of the variables have the value of `True` by the end of the program. Python is a dynamic language. That means variables can change the types of data it holds. 

{Check It!|assessment}(multiple-choice-1694007804)
