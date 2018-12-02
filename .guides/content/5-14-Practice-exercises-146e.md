---------

For the exercises below, enter your code in the exercises_3.py file in the left pane, and then click Try It to evaluate it.  When you are ready to submit your answers, enter your responses in the spaces provided below and click Check It or Submit Answer.

1. The <span>time</span> module provides a function, also named <span>time</span>, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

       >>> import time
       >>> time.time()
       1437746094.5735958

{Try It}(python3 code/exercises_3.py)

{Submit Answer!|assessment}(free-text-3367323985)


Fermat’s Last Theorem says that there are no positive integers $a$, $b$, and $c$ such that

   $$a^n + b^n = c^n$$ 

for any values of $n$ greater than 2.

2.  Write a function named `check_fermat` that takes four parameters—<span>a</span>, <span>b</span>, <span>c</span> and <span>n</span>—and checks to see if Fermat’s theorem holds. If $n$ is greater than 2 and

    $$a^n + b^n = c^n$$ the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

3.  Write a function that prompts the user to input values for <span>a</span>, <span>b</span>, <span>c</span> and <span>n</span>, converts them to integers, and uses `check_fermat` to check whether they violate Fermat’s theorem.

{Try It}(python3 code/exercises_3.py)


If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle:

> If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)

4.  Write a function named `is_triangle` that takes three integers as arguments, and that prints either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths.

5.  Write a function that prompts the user to input three stick lengths, converts them to integers, and uses `is_triangle` to check whether sticks with the given lengths can form a triangle.
 
6. What is the output of the following program? Draw a stack diagram that shows the state of the program when it prints the result.

       def recurse(n, s):
           if n == 0:
               print(s)
           else:
               recurse(n-1, n+s)

       recurse(3, 0)
    
{Try It}(python3 code/exercises_3.py)
    

7.  {Submit Answer!|assessment}(free-text-3828640500)


8. {Submit Answer!|assessment}(free-text-1474599446)


The following exercises use the <span>turtle</span> module, described in Chapter 4:

Read the following function and see if you can figure out what it does (see the examples in Chapter 4). Then run it and see if you got it right.

    def draw(t, length, n):
        if n == 0:
            return
        angle = 50
        t.fd(length*n)
        t.lt(angle)
        draw(t, length, n-1)
        t.rt(2*angle)
        draw(t, length, n-1)
        t.lt(angle)
        t.bk(length*n)

![image](/.guides/img/koch.jpg)



The Koch curve is a fractal that looks something like Figure . To draw a Koch curve with length $x$, all you have to do is

1.  Draw a Koch curve with length $x/3$.

2.  Turn left 60 degrees.

3.  Draw a Koch curve with length $x/3$.

4.  Turn right 120 degrees.

5.  Draw a Koch curve with length $x/3$.

6.  Turn left 60 degrees.

7.  Draw a Koch curve with length $x/3$.

The exception is if $x$ is less than 3: in that case, you can just draw a straight line with length $x$.

9.  Write a function called <span>koch</span> that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.

10.  Write a function called <span>snowflake</span> that draws three Koch curves to make the outline of a snowflake.

    Solution: <http://thinkpython2.com/code/koch.py>.

11.  The Koch curve can be generalized in several ways. See <http://en.wikipedia.org/wiki/Koch_snowflake> for examples and implement your favorite.

