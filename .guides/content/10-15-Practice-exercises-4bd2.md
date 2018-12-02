---------

You can download solutions to these exercises from <http://thinkpython2.com/code/list_exercises.py>.

1. Write a function called `nested_sum` that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:

       >>> t = [[1, 2], [3], [4, 5, 6]]
       >>> nested_sum(t)
       21


2. Write a function called <span>cumsum</span> that takes a list of numbers and returns the cumulative sum; that is, a new list where the $i$th element is the sum of the first $i+1$ elements from the original list. For example:

       >>> t = [1, 2, 3]
       >>> cumsum(t)
       [1, 3, 6]

{Try It}(python3 code/lists_exercises.py)

3. Write a function called `middle` that takes a list and returns a new list that contains all but the first and last elements. For example:

       >>> t = [1, 2, 3, 4]
       >>> middle(t)
       [2, 3]

4. Write a function called `chop` that takes a list, modifies it by removing the first and last elements, and returns <span>None</span>. For example:

       >>> t = [1, 2, 3, 4]
       >>> chop(t)
       >>> t
       [2, 3]

5. Write a function called `is_sorted` that takes a list as a parameter and returns <span>True</span> if the list is sorted in ascending order and <span>False</span> otherwise. For example:

       >>> is_sorted([1, 2, 2])
       True
       >>> is_sorted(['b', 'a'])
       False
    

6. Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called `is_anagram` that takes two strings and returns <span>True</span> if they are anagrams.

7. Write a function called `has_duplicates` that takes a list and returns <span>True</span> if there is any element that appears more than once. It should not modify the original list.

{Try It}(python3 code/lists_exercises.py)



Solution: <http://thinkpython2.com/code/wordlist.py>.

