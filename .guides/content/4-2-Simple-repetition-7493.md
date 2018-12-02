-----------------

Chances are you wrote something like this:

    bob.fd(100)
    bob.lt(90)

    bob.fd(100)
    bob.lt(90)

    bob.fd(100)
    bob.lt(90)

    bob.fd(100)

We can do the same thing more concisely with a <span>for</span> statement. Add this example to <span>turtle_exercise_1.py</span> and run it again:

    for i in range(4):
        print('Hello!')

{Try It}(sh .guides/bg.sh python3 code/turtle_exercise_1.py)

You should see something like this:

    Hello!
    Hello!
    Hello!
    Hello!

This is the simplest use of the <span>for</span> statement; we will see more later. But that should be enough to let you rewrite your square-drawing program. Don’t go on until you do.

Here is a <span>for</span> statement that draws a square:

    for i in range(4):
        bob.fd(100)
        bob.lt(90)

{Try It}(sh .guides/bg.sh python3 code/turtle_exercise_1.py)

The syntax of a <span>for</span> statement is similar to a function definition. It has a header that ends with a colon and an indented body. The body can contain any number of statements.

A <span>for</span> statement is also called a <span>**loop**</span> because the flow of execution runs through the body and then loops back to the top. In this case, it runs the body four times.

This version is actually a little different from the previous square-drawing code because it makes another turn after drawing the last side of the square. The extra turn takes more time, but it simplifies the code if we do the same thing every time through the loop. This version also has the effect of leaving the turtle back in the starting position, facing in the starting direction.

