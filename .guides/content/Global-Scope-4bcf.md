## Global Scope

To recap, all variables have scope. Variables declared in the program have global scope, variables declared in a function have local scope. Global and local variables can have the same name, but be independent of each other. Global variables can be "seen" inside function, but cannot be modified. 

The `global` keyword allows you to modify global variables inside a function. In the image below, there is no more distinction between the red and blue areas. `global` removes the blue area, and there is only one version of `my_var`. That is why the output is `inner scope` and `inner scope`.

![Global Scope](.guides/images/global-scope.png)

```python
my_var = "outer scope"

def print_scope():
    global my_var
    my_var = "inner scope"
    print(my_var)

print_scope()
print(my_var)
```

{try it}(python3 code/functions/global-scope.py 1)

|||challenge
## What happens if you:
* Remove the line of code from inside the function that says `my_var = "inner scope"`?
* Type `my_var = "inner scope"` inside the function, but remove it from the first line of the program?
* Make the code look like this:
```python
def print_scope():
    global my_var
    my_var = "inner scope"
    print(my_var)

print(my_var)
print_scope()
```

|||

{try it}(python3 code/functions/global-scope.py 2)

{Check It!|assessment}(multiple-choice-1787984748)
