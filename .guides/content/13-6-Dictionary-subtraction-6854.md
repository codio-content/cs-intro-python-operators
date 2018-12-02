----------------------

Finding the words from the book that are not in the word list from <span>words.txt</span> is a problem you might recognize as set subtraction; that is, we want to find all the words from one set (the words in the book) that are not in the other (the words in the list).

<span>`subtract`</span> takes dictionaries <span>d1</span> and <span>d2</span> and returns a new dictionary that contains all the keys from <span>d1</span> that are not in <span>d2</span>. Since we don’t really care about the values, we set them all to None.

    def subtract(d1, d2):
        res = dict()
        for key in d1:
            if key not in d2:
                res[key] = None
        return res

To find the words in the book that are not in <span>words.txt</span>, we can use `process_file` to build a histogram for <span>words.txt</span>, and then subtract:

    words = process_file('words.txt')
    diff = subtract(hist, words)

    print("Words in the book that aren't in the word list:")
    for word in diff:
        print(word, end=' ')

Here are some of the results from <span>*Emma*</span>:

    Words in the book that aren't in the word list:
    rencontre jane's blanche woodhouses disingenuousness 
    friend's venice apartment ...

Some of these words are names and possessives. Others, like “rencontre”, are no longer in common use. But a few are common words that should really be in the list!

6. Python provides a data structure called <span>`set`</span> that provides many common set operations. You can read about them in Section 19.5, or read the documentation at <http://docs.python.org/3/library/stdtypes.html#types-set>.

   Write a program that uses set subtraction to find words in the book that are not in the word list. Solution: <http://thinkpython2.com/code/analyze_book2.py>.

