---------

[wordlist2]

Write a function that reads the words in <span>words.txt</span> and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the <span>in</span> operator as a fast way to check whether a string is in the dictionary.

If you did Exercise [wordlist1], you can compare the speed of this implementation with the list <span>in</span> operator and the bisection search.

[setdefault]

Read the documentation of the dictionary method <span>setdefault</span> and use it to write a more concise version of `invert_dict`. Solution: <http://thinkpython2.com/code/invert_dict.py>.

Memoize the Ackermann function from Exercise [ackermann] and see if memoization makes it possible to evaluate the function with bigger arguments. Hint: no. Solution: <http://thinkpython2.com/code/ackermann_memo.py>.

If you did Exercise [duplicate], you already have a function named `has_duplicates` that takes a list as a parameter and returns <span>True</span> if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of `has_duplicates`. Solution: <http://thinkpython2.com/code/has_duplicates.py>.

{Try It}(python3 code/dictionary_1.py)




