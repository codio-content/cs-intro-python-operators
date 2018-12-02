---------

1. Draw a stack diagram for the following program. 

    def b(z):
        prod = a(z, z)
        print(z, prod)
        return prod

    def a(x, y):
        x = x + 1
        return x * y

    def c(x, y, z):
        total = x + y + z
        square = b(total)**2
        return square

    x = 1
    y = x + 1
    print(c(x, y+3, x+y))
    
{Submit Answer!|assessment}(free-text-1222847010)


2. Use the exercises_4.py file in the top left pane to complete the following exercise.

   The Ackermann function, $A(m, n)$, is defined:

$$\begin{aligned}
A(m, n) = \begin{cases} 
              n+1 & \mbox{if } m = 0 \\ 
        A(m-1, 1) & \mbox{if } m > 0 \mbox{ and } n = 0 \\ 
A(m-1, A(m, n-1)) & \mbox{if } m > 0 \mbox{ and } n > 0.
\end{cases} \end{aligned}$$

See <http://en.wikipedia.org/wiki/Ackermann_function>. Write a function named <span>ack</span> that evaluates the Ackermann function. Use your function to evaluate <span>ack(3, 4)</span>, which should be 125. What happens for larger values of <span>m</span> and <span>n</span>? Solution: <http://thinkpython2.com/code/ackermann.py>.

{Try It}(python3 code/exercises_4.py)


Use the palindrome.py file in the bottom left pane to complete the following exercises.

A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

   The following are functions that take a string argument and return the first, last, and middle letters:

       def first(word):
           return word[0]

       def last(word):
           return word[-1]

       def middle(word):
           return word[1:-1]

   We’ll see how they work in Chapter 8.

4.  Type these functions into the file named <span>palindrome.py</span> and test them out. What happens if you call <span>middle</span> with a string with two letters? One letter? What about the empty string, which is written `''` and contains no letters?

{Try It}(python3 code/palindrome.py)

5.  Write a function called `is_palindrome` that takes a string argument and returns <span>True</span> if it is a palindrome and <span>False</span> otherwise. Remember that you can use the built-in function <span>len</span> to check the length of a string.

Solution: <http://thinkpython2.com/code/palindrome_soln.py>.



