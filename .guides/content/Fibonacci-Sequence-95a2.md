----------

## Fibonacci Number

A Fibonacci number is a number in which the current number is the sum of the previous two Fibonacci numbers.

![Fibonacci Sequence](.guides/images/fibonacci.png)

Calculating a Fibonacci number is self-similar, which means it can be define with recursion. Setting the base case is important to avoid infinite recursion. When the number `n` is 0 the Fibonacci number is 0, and when `n` is 1 the Fibonacci number is 1. So if `n` is less than or equal to 1, then return `n`. That is the base case.

```python
def fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
      
print(fibonacci(3))
```

[Code Visualizer](open_tutor code/functions/fibonacci.py)
{try it}(python3 code/functions/fibonacci.py 1)

|||challenge
## What happens if you:
* Change the print statment to `print(fibonacci(0))`?
* Change the print statment to `print(fibonacci(8))`?
* Change the print statment to `print(fibonacci(100))`?

|||

[Code Visualizer](open_tutor code/functions/fibonacci.py)
{try it}(python3 code/functions/fibonacci.py 2)

## Fibonacci Sequence

Fibonacci numbers are most often talked about as a sequence. The code below adds the functionality of printing a Fibonacci sequence of predetermined length.

```python
def fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
      
fibonacci_length = 10
for num in range(fibonacci_length):
    print(fibonacci(num))
```

[Code Visualizer](open_tutor code/functions/fibonacci.py)
{try it}(python3 code/functions/fibonacci.py 3)

|||challenge
## What happens if you:
* Change `fibonacci_length` to 38?
* Change `fibonacci_length` to 39?

|||

[Code Visualizer](open_tutor code/functions/fibonacci.py)
{try it}(python3 code/functions/fibonacci.py 4)

{Check It!|assessment}(multiple-choice-3252681714)
