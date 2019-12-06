----------

## What is Recursion?

Solving a coding problem with functions involves breaking down the problem into smaller problems. When these smaller problems are variations of the larger problem (also know as self-similar), then recursion can be used. For example, the mathematical function factorial is self-similar. Five factorial (`5!`) is calculated as `5 * 4 * 3 * 2 * 1`. Mouse over the image below to see that `5!` is really just `5 * 4!`, and `4!` is really just `4 * 3!` and so on.

<div class="recursion"></div>

Because `5!` is self-similar, recursion can be used to calculate the answer. Recursive functions are functions that call themselves. Use the Code Visualizer to see how Python handles this recursive function.

```python
def factorial(n):
    """Calculate factorial recursively"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
```

[Code Visualizer](open_tutor code/functions/what-is-recursion.py)
{try it}(python3 code/functions/what-is-recursion.py 1)

Recursion is an abstract and difficult topic, so it might be a bit hard to follow what is going on here. When `n` is 5, Python starts a multiplication problem of `5 * factorial(4)`. The function runs again and the multiplication problem becomes `5 * 4 * factorial(3)`. This continues until `n` is 1. Python returns the value `1`, and Python solves the multiplication problem `5 * 4 * 3 * 2 * 1`. The video below should help explain how `5!` is calculated recursively. 

<video src=".guides/video/recursion-video.m4v" class="recursion-video" controls></video>

## The Base Case

Each recursive function has two parts: the recursive case (where the function calls itself with a different parameter) and the base case (where the function stops calling itself and returns a value).

![Cases for Recursion](.guides/images/recursive-cases.png)

The base case is the most important part of a recursive function. Without it, the function will never stop calling itself. Like an infinite loop, Python will stop the program with an error.

```python
def factorial(n):
    """Recursion without a base case"""
    return n * factorial(n - 1)
    
print(factorial(5))
```

[Code Visualizer](open_tutor code/functions/what-is-recursion.py)
{try it}(python3 code/functions/what-is-recursion.py 2)

Always start with the base case when creating a recursive function. Each time the function is called recursively, the program should get one step closer to the base case.

|||challenge
## What happens if you:
* Add a base case for the `factorial` function?
* Change the print statement to `print(factorial(0))`?

Modify the base case so that `factorial(0)` does not result in an error. Test your new base case with a negative number.
<details><summary>**Solution**</summary>The [factorial operation](https://en.wikipedia.org/wiki/Factorial) only works with positive integers. So the base case should be `if n <= 0:`.</details>

|||

[Code Visualizer](open_tutor code/functions/what-is-recursion.py)
{try it}(python3 code/functions/what-is-recursion.py 3)

{Check It!|assessment}(multiple-choice-984962408)
