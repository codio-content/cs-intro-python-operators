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
* Change `fibonacci_length` to 30?
* Change `fibonacci_length` to 50?

|||

[Code Visualizer](open_tutor code/functions/fibonacci.py)
{try it}(python3 code/functions/fibonacci.py 4)

<details><summary>**Why is Python timing out?**</summary>The code written above is terribly inefficient. Each time through the loop, Python is calculating the same Fibonacci numbers again and again. When `num` is 1, Python calculates the Fibonacci numbers for 0 and 1. When `num` is 2, Python is calculating the Fibonacci numbers for 0, 1, and 2. Once `num` becomes large enough, it becomes too much work for Python to have to recalcuate these large numbers over and over again. There is a more efficient way to do this by using a data structure called a dictionary. The idea is to store previously calculated Fibonacci numbers in the dictionary. So instead of recalculating the same numbers again and again, you can get these numbers from the dictionary. If a Fibonacci number is not in the dictionary, then calculate it and add it to the dictionary. Data structures are a bit beyond the scope of these lessons, but here is the code of a more efficient way to calculate and print the Fibonacci sequence. [Fibonacci sequence with a dictionary](open_file .guides/example-code/fibonacci_example.py)

{Check It!|assessment}(multiple-choice-3252681714)
