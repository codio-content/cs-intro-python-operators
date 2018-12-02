-----------------------

We saw conditional statements in Section 15.4. Conditional statements are often used to choose one of two values; for example:

    if x > 0:
        y = math.log(x)
    else:
        y = float('nan')

This statement checks whether <span>x</span> is positive. If so, it computes <span>math.log</span>. If not, <span>math.log</span> would raise a ValueError. To avoid stopping the program, we generate a “NaN”, which is a special floating-point value that represents “Not a Number”.

We can write this statement more concisely using a <span>**conditional expression**</span>:

    y = math.log(x) if x > 0 else float('nan')

You can almost read this line like English: “<span>y</span> gets log-<span>x</span> if <span>x</span> is greater than 0; otherwise it gets NaN”.

Recursive functions can sometimes be rewritten using conditional expressions. For example, here is a recursive version of <span>factorial</span>:

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

We can rewrite it like this:

    def factorial(n):
        return 1 if n == 0 else n * factorial(n-1)

Another use of conditional expressions is handling optional arguments. For example, here is the init method from <span>GoodKangaroo</span> (see Exercise in Chapter 17):

        def __init__(self, name, contents=None):
            self.name = name
            if contents == None:
                contents = []
            self.pouch_contents = contents

We can rewrite this one like this:

        def __init__(self, name, contents=None):
            self.name = name
            self.pouch_contents = [] if contents == None else contents 

In general, you can replace a conditional statement with a conditional expression if both branches contain simple expressions that are either returned or assigned to the same variable.

