---------

Read the documentation of the string methods at <http://docs.python.org/3/library/stdtypes.html#string-methods>. You might want to experiment with some of them to make sure you understand how they work. <span>`strip`</span> and <span>`replace`</span> are particularly useful.

The documentation uses a syntax that might be confusing. For example, in `find(sub[, start[, end]])`, the brackets indicate optional arguments. So <span>sub</span> is required, but <span>start</span> is optional, and if you include <span>start</span>, then <span>end</span> is optional.

There is a string method called <span>count</span> that is similar to the function in Section 8.7. Read the documentation of this method and write an invocation that counts the number of <span>a</span>’s in `'banana'`.

A string slice can take a third index that specifies the “step size”; that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

    >>> fruit = 'banana'
    >>> fruit[0:5:2]
    'bnn'

A step size of -1 goes through the word backwards, so the slice `[::-1]` generates a reversed string.

Use this idiom to write a one-line version of `is_palindrome` from Chapter 6.

{Try It}(python3 code/new_palindrome.py)

The following functions are all <span>*intended*</span> to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).

{Submit Answer!|assessment}(free-text-3413124657)


{Submit Answer!|assessment}(free-text-180072190)


{Submit Answer!|assessment}(free-text-920992499)


{Submit Answer!|assessment}(free-text-2821882119)


{Submit Answer!|assessment}(free-text-2364923939)



