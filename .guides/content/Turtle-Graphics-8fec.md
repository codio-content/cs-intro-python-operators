----------
Before continuing with loops, we are going to learn how to create graphical output with the **turtle library**. Like a pencil on paper, the turtle object leaves a line as it moves around the screen.

## Turtle Syntax
You need to import the turtle library as the first line of your code and end your code by calling `mainloop()`.

```python
import turtle

# All of your turtle commands
# go in this space here.

turtle.mainloop()
```

The next step is to create a turtle object to move around the screen.

```python
import turtle

t = turtle.Turtle() # create a turtle called t

# All of your turtle commands
# go in this space here.

turtle.mainloop()
```

Here are some basic commands to use with the turtle library.

|Command|Parameter|Description|
|:-----:|:-------:|:---------:|
|`t.forward(n)`|Where `n` represents the number of pixels|Move the turtle forward|
|`t.backward(n)`|Where `n` represents the number of pixels|Move the turtle backward|
|`t.rt(d)`|Where `d` represents the number of degrees|Turn the turtle to the right|
|`t.lt(d)`|Where `d` represents the number of degrees|Turn the turtle to the left|

Go ahead and get comfortable creating and moving a turtle around the screen before we start drawing with loops.

|||definition
### Turtle Output
Click the button below to run your code. You may have noticed that there is no `print` command used with turtle objects, so the output of your program does not appear as you would expect. Look for the tab that reads **Preview https/...** and click on it. You should see your turtle drawing there. Close the window with the turtle output to stop your program.
|||

{Try it|terminal}(sh .guides/bg.sh python3 code/loops/playground-turtle-1.py)
