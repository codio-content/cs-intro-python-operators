---------

Breaking a large program into smaller functions creates natural checkpoints for debugging. If a function is not working, there are three possibilities to consider:

-   There is something wrong with the arguments the function is getting; a precondition is violated.

-   There is something wrong with the function; a postcondition is violated.

-   There is something wrong with the return value or the way it is being used.

To rule out the first possibility, you can add a <span>print</span> statement at the beginning of the function and display the values of the parameters (and maybe their types). Or you can write code that checks the preconditions explicitly.

If the parameters look good, add a <span>print</span> statement before each <span>return</span> statement and display the return value. If possible, check the result by hand. Consider calling the function with values that make it easy to check the result (as in Section [incremental.development]).

If the function seems to be working, look at the function call to make sure the return value is being used correctly (or used at all!).

Adding print statements at the beginning and end of a function can help make the flow of execution more visible. For example, here is a version of <span>factorial</span> with print statements:

    def factorial(n):
        space = ' ' * (4 * n)
        print(space, 'factorial', n)
        if n == 0:
            print(space, 'returning 1')
            return 1
        else:
            recurse = factorial(n-1)
            result = n * recurse
            print(space, 'returning', result)
            return result

<span>space</span> is a string of space characters that controls the indentation of the output. Here is the result of <span>factorial(4)</span> :

                     factorial 4
                 factorial 3
             factorial 2
         factorial 1
     factorial 0
     returning 1
         returning 1
             returning 2
                 returning 6
                     returning 24

If you are confused about the flow of execution, this kind of output can be helpful. It takes some time to develop effective scaffolding, but a little bit of scaffolding can save a lot of debugging.

