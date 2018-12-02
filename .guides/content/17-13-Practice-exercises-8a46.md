---------

Using Time2.py, change the attributes of <span>Time</span> to be a single integer representing seconds since midnight. Then modify the methods (and the function `int_to_time`) to work with the new implementation. You should not have to modify the test code in <span>main</span>. When you are done, the output should be the same as before. 

{Try It}(python3 code/Time2.py)

Solution: <http://thinkpython2.com/code/Time2_soln.py>.



This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python. Write a definition for a class named <span>Kangaroo</span> with the following methods:

1.  An `__init__` method that initializes an attribute named `pouch_contents` to an empty list.

2.  A method named `put_in_pouch` that takes an object of any type and adds it to `pouch_contents`.

3.  A `__str__` method that returns a string representation of the Kangaroo object and the contents of the pouch.

Test your code by creating two <span>Kangaroo</span> objects, assigning them to variables named <span>kanga</span> and <span>roo</span>, and then adding <span>roo</span> to the contents of <span>kanga</span>’s pouch.



View BadKangaroo.py. It contains a solution to the previous problem with one big, nasty bug. Find and fix the bug.

{Try It}(python3 code/BadKangaroo.py)

If you get stuck, you can download <http://thinkpython2.com/code/GoodKangaroo.py>, which explains the problem and demonstrates a solution.

