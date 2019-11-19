----------
While loops differ from for loops in several ways. 

|While Loop|For Loop|
|----------|--------|
|Runs as long as a **condition** is true|Runs a predetermined amount of times|
|You must declare a counting variable|Counting variable is automatically declared|
|You must increment the counting variable|The counting variable is already incremented|

## While Loop Syntax
While loops, just like for loops, use a `:` and indent for all commands that should be repeated. Here is a while loops that prints "Hello" five times.

```python
count = 0 # counting variable
while count < 5:
    print("Hello")
    count = count + 1
```

[Code Visualizer](open_tutor code/loops/playground-while-loop.py)
{Try it}(python3 code/loops/playground-while-loop.py 1)

|||challenge
## What happens if you:
* Change the while statement to `while count < 10:`?
* Change the last line of code to `count = count + 2`?
* Change the while statement to `while count < 0:`?

|||

## Infinite Loops
Infinite loops are loops that never have a test condition that causes the loop to stop. For example, this is a common mistake:

```python
count = 0 # counting variable
while count < 5:
    print("Hello")
```

Since the variable `count` never gets incremented. It remains 0, and 0 will forever be less than 5. So the loop will never stop.

|||warning
Run the code above to see what happens. Python will eventually stop the loop due to an output limit, but it will take some time before this happens. Since for loops run for a predetermined amount of time, you do not see infinite loops with them.
|||

{Try it}(python3 code/loops/playground-while-loop.py 2)

## Why Use a While Loop?
If a while loop does the same thing as a for loop and infinite loops can occur in a while loop, why use them? While loops are useful when you are waiting for a certain event to occur. Imagine you are making a video game. The game should continue until the player loses all of their lives. You don't know how long this will take, so a while loop would be appropriate.

```python
player_lives = 3

while player_lives > 0:
    # video game code
    # goes here
```