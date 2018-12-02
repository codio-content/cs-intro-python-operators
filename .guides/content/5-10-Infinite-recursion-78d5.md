------------------

If a recursion never reaches a base case, it goes on making recursive calls forever, and the program never terminates. This is known as <span>**infinite recursion**</span>, and it is generally not a good idea. Here is a minimal program with an infinite recursion:

    def recurse():
        recurse()

In most programming environments, a program with infinite recursion does not really run forever. Python reports an error message when the maximum recursion depth is reached:

      File "<stdin>", line 2, in recurse
      File "<stdin>", line 2, in recurse
      File "<stdin>", line 2, in recurse
                      .   
                      .
                      .
      File "<stdin>", line 2, in recurse
    RuntimeError: Maximum recursion depth exceeded

This traceback is a little bigger than the one we saw in the previous chapter. When the error occurs, there are 1000 <span>recurse</span> frames on the stack!

If you encounter an infinite recursion by accident, review your function to confirm that there is a base case that does not make a recursive call. And if there is a base case, check whether you are guaranteed to reach it.

