---------

1. Write a function named `right_justify` that takes a string named <span>s</span> as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.


       >>> right_justify('monty')
                                                                     monty

Hint: Use string concatenation and repetition. Also, Python provides a built-in function called <span>len</span> that returns the length of a string, so the value of `len('monty')` is 5.

{Try It}(python3 code/function_exercises.py)

2. A function object is a value you can assign to a variable or pass as an argument. For example, `do_twice` is a function that takes a function object as an argument and calls it twice:

       def do_twice(f):
           f()
           f()

Here’s an example that uses `do_twice` to call a function named `print_spam` twice.

    def print_spam():
        print('spam')

    do_twice(print_spam)

2.1  Type this example into a script and test it.  NOTE: replace your existing code in the file on the left.

{Try It}(python3 code/function_exercises.py)

2.2  Modify `do_twice` so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.

{Try It}(python3 code/function_exercises.py)

2.3  Copy the definition of `print_twice` from earlier in this chapter to your script.

2.4  Use the modified version of `do_twice` to call `print_twice` twice, passing `'spam'` as an argument.

{Try It}(python3 code/function_exercises.py)

2.5  Define a new function called `do_four` that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

{Try It}(python3 code/function_exercises.py)

Solution: <http://thinkpython2.com/code/do_four.py>.

3. Note: This exercise should be done using only the statements and other features we have learned so far.

3.1  Write a function that draws a grid like the following:

        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +

   Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

        print('+', '-')

   By default, <span>print</span> advances to the next line, but you can override that behavior and put a space at the end, like this:

        print('+', end=' ')
        print('-')

   The output of these statements is `'+ -'` on the same line. The output from the next print statement would begin on the next line.
    
 {Try It}(python3 code/function_exercises.py)

3.2  Write a function that draws a similar grid with four rows and four columns.

{Try It}(python3 code/function_exercises.py)

Solution: <http://thinkpython2.com/code/grid.py>. Credit: This exercise is based on an exercise in Oualline, <span>*Practical C Programming, Third Edition*</span>, O’Reilly Media, 1997.

