## Lab 1 - Recursive Tree

![Recursive Tree](.guides/images/fractal_tree.png)

Trees can be drawn recursively. Draw a branch. At the end of the branch, draw two smaller branches with one to the left and the other to the right. Repeat until a certain condition is true. This program will walk you through drawing a tree in this way.

Start by importing the `turtle` module. Declare a turtle object, and define the function `recursive_tree`. This function should take three parameters, `branch_length`, `angle`, and `t`. Use `pass` as the function body for now. Finally, use `turtle.mainlooop()` at the end of the program.

```python
import turtle

t = turtle.Turtle()

def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    pass
  
turtle.mainloop()
```

The base case for this function is a bit different. In previous examples, if the base case is true a value was returned. The function `recursive_tree` does not return a value, it draws on the screen. So the base case will be to keep recursing as long as `branch_length` is greater than some value. Define the base case as `branch_length` as being greater than 5. Use `pass` for the body of the conditional.

```python
def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        pass
```

Start drawing the tree by going forward and turning right. Call `recursive_tree` again, but reduce `branch_length` by 15. The code should run, but the tree will not look like a tree. It looks more like a curve made of series of line segments decreasing in size.

```python
def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        recursive_tree(branch_length - 15, angle, t)
```

[Code Visualizer](open_tutor code/recursion/recursive_tree.py)
{Try it|terminal}(sh .guides/bg.sh python3 code/recursion/recursive_tree.py)

The next step is to draw the branch that goes off to the left. Since the turtle turned to the right the number of degrees that the parameter `angle` represents, the turtle needs to turn to the left twice the degrees of `angle`. Turning to the left `angle` will put the turtle back at its original heading. The turtle needs to go further to the left. Then draw another branch whose length is reduced by 15.

```python
def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        recursive_tree(branch_length - 15, angle, t)
        t.left(angle * 2)
        recursive_tree(branch_length - 15, angle, t)
```

[Code Visualizer](open_tutor code/recursion/recursive_tree.py)
{Try it|terminal}(sh .guides/bg.sh python3 code/recursion/recursive_tree.py)

The tree is looking better, but there are two more things that need to be done. First, put the turtle back to its original heading by turning right `angle` degrees. Then go backwards the length of the branch. Call the `recursive_tree` function to draw a tree.

```python
def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        recursive_tree(branch_length - 15, angle, t)
        t.left(angle * 2)
        recursive_tree(branch_length - 15, angle, t)
        t.right(angle)
        t.backwards(branch_length)
        
recursive_tree(45, 20, t)
```

[Code Visualizer](open_tutor code/recursion/recursive_tree.py)
{Try it|terminal}(sh .guides/bg.sh python3 code/recursion/recursive_tree.py)

|||challenge
## What happens if you:
* Increase the branch length when calling `recursive_tree` for the first time?
* Increase and decrease the angle when calling `recursive_tree` for the first time?
* When decreasing `branch_length`, change 15 to something smaller (be sure to change all of the 15's)?
* Change the base case to `if branch_length > 1:`?
* Rotate the turtle 90 degrees to the left before calling `recursive_tree` for the first time?

|||

[Code Visualizer](open_tutor code/recursion/recursive_tree.py)
{Try it|terminal}(sh .guides/bg.sh python3 code/recursion/recursive_tree.py)

<details><summary>**Solution**</summary>[Recursive tree solution](open_file .guides/secure/recursive_tree_solution.py panel=0)</details>

{Check It!|assessment}(multiple-choice-1551096855)
