---------------------

A second form of the <span>if</span> statement is “alternative execution”, in which there are two possibilities and the condition determines which one runs. The syntax looks like this:

    if x % 2 == 0:
        print('x is even')
    else:
        print('x is odd')

If the remainder when <span>x</span> is divided by 2 is 0, then we know that <span>x</span> is even, and the program displays an appropriate message. If the condition is false, the second set of statements runs. Since the condition must be true or false, exactly one of the alternatives will run. The alternatives are called <span>**branches**</span>, because they are branches in the flow of execution.

