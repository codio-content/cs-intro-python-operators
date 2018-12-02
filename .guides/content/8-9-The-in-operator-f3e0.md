----------------------------

The word <span>`in`</span> is a boolean operator that takes two strings and returns <span>True</span> if the first appears as a substring in the second:

    >>> 'a' in 'banana'
    True
    >>> 'seed' in 'banana'
    False

For example, the following function prints all the letters from <span>word1</span> that also appear in <span>word2</span>:

    def in_both(word1, word2):
        for letter in word1:
            if letter in word2:
                print(letter)

With well-chosen variable names, Python sometimes reads like English. You could read this loop, “for (each) letter in (the first) word, if (the) letter (appears) in (the second) word, print (the) letter.”

Here’s what you get if you compare apples and oranges:

    >>> in_both('apples', 'oranges')
    a
    e
    s

