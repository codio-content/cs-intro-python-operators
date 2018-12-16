---------------
A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

   The following are functions that take a string argument and return the first, last, and middle letters:

       def first(word):
           return word[0]

       def last(word):
           return word[-1]

       def middle(word):
           return word[1:-1]

   We’ll see how they work in Chapter 8.

1.  Type these functions into the file named <span>palindrome.py</span> and test them out. What happens if you call <span>middle</span> with a string with two letters? One letter? What about the empty string, which is written `''` and contains no letters?

{Try It}(python3 code/palindrome.py)

2.  Write a function called `is_palindrome` that takes a string argument and returns <span>True</span> if it is a palindrome and <span>False</span> otherwise. Remember that you can use the built-in function <span>len</span> to check the length of a string.

Solution: <http://thinkpython2.com/code/palindrome_soln.py>.
