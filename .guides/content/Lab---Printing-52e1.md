
## Tutorial Lab 1: Printing

1) Use the code editor to the left.
2) Enter the code below.

```python
my_variable = 'I am learning' #step 1
print(my_variable, end='') #step 2
my_variable = " to program" #step 3
print(my_variable, end="") #step 4
my_variable = " in Python." #step 5
print(my_variable) #step 6
my_variable = "Hooray!" #step 7
print(my_variable) #step 8
```
3) Run the module to see the output. Use the code visualizer to go through the program step by step.

[Code Visualizer](open_tutor code/fundamentals/lab-print.py)
{try it}(python3 code/fundamentals/lab-print.py)

4) Here are some important points about the program (click on the underlined text):
    * [Step 1](open_file code/fundamentals/lab-print.py panel=0 ref="#step 1" count=1) - Declare the variable `my_variable` and assign it the value `I am learning`.
    * [Step 2](open_file code/fundamentals/lab-print.py panel=0 ref="#step 2" count=1) - Remove the newline character with `end=''`.
    * [Step 3](open_file code/fundamentals/lab-print.py panel=0 ref="#step 3" count=1) - Add a space when starting the string to avoid `learningto`
    * [Step 4](open_file code/fundamentals/lab-print.py panel=0 ref="#step 4" count=1) - A double quote can be used with `end=` and not cause an error
    * [Step 5](open_file code/fundamentals/lab-print.py panel=0 ref="#step 5" count=1) - Double quotes can be used to define a string
    * [Step 6](open_file code/fundamentals/lab-print.py panel=0 ref="#step 6" count=1) - A newline character is added since there is no `end=''`
    * [Step 8](open_file code/fundamentals/lab-print.py panel=0 ref="#step 8" count=1) - `Hooray!` is on its own line since a regular `print` command was used in step 6
    
{Check It!|assessment}(multiple-choice-976098584)
