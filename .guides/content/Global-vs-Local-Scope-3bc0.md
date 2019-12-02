## Global vs Local Scope

If there is a collision of local and global variables in a function, the local variable will always take precedence. The global `my_var` (the red one) exists only in the light red area. The local `my_var` (the blue one) exists only in the light blue area. The blue `my_var` is independent of the red `my_var`. That is why the output of the program is two different strings.

![Variable Scope](.guides/images/variable-scope.png)

```python
my_var = "global scope"

def print_scope():
    """Demonstrate local scope vs global scope"""
    my_var = "local scope"
    print(my_var)

print_scope()
print(my_var)
```

{try it}(python3 code/functions/variable-scope.py 1)

The exception to this rule is when the `global` keyword is being used. In this case, the global variable takes precedence. 

```python
my_var = "global scope"

def print_scope():
    """Demonstrate local scope vs global scope"""
    global my_var
    my_var = "local scope"
    print(my_var)

print_scope()
print(my_var)
```

{try it}(python3 code/functions/variable-scope.py 2)


|||challenge
## What happens if you:
* Add the parameter `my_var` to the `print_scope` function and pass `my_var` to `print_scope` in the function call?
```python
my_var = "global scope"

def print_scope(my_var):
    """Demonstrate local scope vs global scope"""
    my_var = "local scope"
    print(my_var)

print_scope(my_var)
print(my_var)
```

|||

{try it}(python3 code/functions/variable-scope.py 3)

{Check It!|assessment}(fill-in-the-blanks-1907306637)
