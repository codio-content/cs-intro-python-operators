----------

## Local Scope

Take a look at the code below. The first function declares the variable `my_var` and then prints it. The second function also prints `my_var`. What do you think the output will be?

```python
def function_1():
    my_var = "Hello"
    print(my_var)
    
def function_2():
    print(my_var)
    
function_1()
function_2()
```

{try it}(python3 code/functions/local-scope.py 1)

Python says the problem is that `my_var` is not defined even though the variable is defined on line 3. Variables declared inside a function have local scope. That means `my_var` only "exists" in `function_1`, it cannot be referenced outside of its function. In the image below, light blue box represents the scope of `my_var`. Since `function_2` is outside the scope of `my_var` an error occurs.

![Local Scope](.guides/images/local-scope.png)

|||challenge
## What happens if you:
* Change `function_2` to look like this:
```python
def function_2():
    my_var2 = "Hello"
    print(my_var2)
```

|||

{try it}(python3 code/functions/local-scope.py 2)

## More Local Scope

Each function has its own local scope. That means you can declare two variables with the same name as long as they are in separate functions. The red `my_var` exists only in the light red box, and the blue `my_var` exists only in the light blue box. The boundaries of local scope keep Python from overwriting the value of the first variable with the contents of the second.

![Local Scope](.guides/images/local-scope2.png)

```python
def function_1():
    my_var = "Hello"
    print(my_var)
    
def function_2():
    my_var = "Bonjour"
    print(my_var)
    
function_1()
function_2()
```

{try it}(python3 code/functions/local-scope.py 3)

|||challenge
## What happens if you:
* Declare and call `function_3`:
```python
def function_3():
    my_var = "Hola"
    print(my_var)
```

|||

{try it}(python3 code/functions/local-scope.py 4)

{Check It!|assessment}(fill-in-the-blanks-908435280)
