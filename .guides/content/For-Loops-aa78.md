----------

## For Loop Syntax
Before you can start writing a loop, you need to be able to spot the pattern. Let's take something simple:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

{Try it}(python3 code/loops/playground-for-loop.py 1) 

The pattern is `print("Hello")`, and it is repeated five times. Since we know that the loops needs to run exactly five times, a for loop is the way to go. Here is how you write a for loop that repeats five times. Use the code [visualizer](open_tutor code/loops/playground-for-loop.py) to see how a for loop works.

```python
for i in range(5):
    print("Hello")
```

[Code Visualizer](open_tutor code/loops/playground-for-loop.py)
{Try it}(python3 code/loops/playground-for-loop.py 2) 

Like **conditionals**, for loops are code blocks. Instead of a **boolean** statement, you use the `range` function followed by a `:`. All of the code that will be repeated needs to be indented.

## Understanding `range`
The expression `range(5)` will return a series of five numbers, but it is important to understand how Python does this. Enter the code below and run it.

```python
for i in range(5):
    print("Loop #" + str(i))
```

[Code Visualizer](open_tutor code/loops/playground-for-loop.py)
{Try it}(python3 code/loops/playground-for-loop.py 3)

The loop ran five times, but the variable `i` did not start with 1. Instead it started with 0. Python, like most programming languages, starts counting with 0. Python will continue counting up to, but not including 5.

|||challenge
## What happens if you:
* Change the print statement to `print("Loop #" + str(i + 1))`?
* Change the range statement to `range(1,6):` and the print statement to `print("Loop #" + str(i))`?
* Change the range statement to `range(0, 10, 2):`?
* Change the range statement to `range(10, 0, -1):`?

|||

[Code Visualizer](open_tutor code/loops/playground-for-loop.py)
{Try it}(python3 code/loops/playground-for-loop.py 4)

<details><summary>**The 3rd Number in `range`**</summary>The range statement normall works with two numbers, where it starts counting and where it ends. The two examples above show that the range statement can take a third number. This number tells `range` the amount to increment. Adding a `2` will mean that `range` counts by 2. Add a negative number and `range` will count down. In this case, be sure that the first number is larger than the second.