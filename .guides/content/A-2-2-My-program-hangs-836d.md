If a program stops and seems to be doing nothing, it is “hanging”. Often that means that it
is caught in an infinite loop or infinite recursion.
• If there is a particular loop that you suspect is the problem, add a print statement
immediately before the loop that says “entering the loop” and another immediately
after that says “exiting the loop”.
Run the program. If you get the first message and not the second, you’ve got an
infinite loop. Go to the “Infinite Loop” section below.
• Most of the time, an infinite recursion will cause the program to run for a while and
then produce a “RuntimeError: Maximum recursion depth exceeded” error. If that
happens, go to the “Infinite Recursion” section below.
If you are not getting this error but you suspect there is a problem with a recursive
method or function, you can still use the techniques in the “Infinite Recursion” section.
• If neither of those steps works, start testing other loops and other recursive functions
and methods.
• If that doesn’t work, then it is possible that you don’t understand the flow of execution
in your program. Go to the “Flow of Execution” section below.
Infinite Loop
If you think you have an infinite loop and you think you know what loop is causing the
problem, add a print statement at the end of the loop that prints the values of the variables
in the condition and the value of the condition.
For example:
while x > 0 and y < 0 :
# do something to x
# do something to y
print('x: ', x)
print('y: ', y)
print("condition: ", (x > 0 and y < 0))
Now when you run the program, you will see three lines of output for each time through
the loop. The last time through the loop, the condition should be False. If the loop keeps
going, you will be able to see the values of x and y, and you might figure out why they are
not being updated correctly.
Infinite Recursion
Most of the time, infinite recursion causes the program to run for a while and then produce
a Maximum recursion depth exceeded error.
If you suspect that a function is causing an infinite recursion, make sure that there is a base
case. There should be some condition that causes the function to return without making a
recursive invocation. If not, you need to rethink the algorithm and identify a base case.
If there is a base case but the program doesn’t seem to be reaching it, add a print statement
at the beginning of the function that prints the parameters. Now when you run the
program, you will see a few lines of output every time the function is invoked, and you
will see the parameter values. If the parameters are not moving toward the base case, you
will get some ideas about why not.
Flow of Execution
If you are not sure how the flow of execution is moving through your program, add print
statements to the beginning of each function with a message like “entering function foo”,
where foo is the name of the function.
Now when you run the program, it will print a trace of each function as it is invoked.