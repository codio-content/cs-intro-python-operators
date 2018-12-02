If you think you have an infinite loop and you think you know what loop is causing the problem, add a <span>print</span> statement at the end of the loop that prints the values of the variables in the condition and the value of the condition.

For example:

    while x > 0 and y < 0 :
        # do something to x
        # do something to y

        print('x: ', x)
        print('y: ', y)
        print("condition: ", (x > 0 and y < 0))

Now when you run the program, you will see three lines of output for each time through the loop. The last time through the loop, the condition should be <span>False</span>. If the loop keeps going, you will be able to see the values of <span>x</span> and <span>y</span>, and you might figure out why they are not being updated correctly.

