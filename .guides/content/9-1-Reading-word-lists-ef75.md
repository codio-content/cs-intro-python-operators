------------------

For the exercises in this chapter we need a list of English words. There are lots of word lists available on the Web, but the one most suitable for our purpose is one of the word lists collected and contributed to the public domain by Grady Ward as part of the Moby lexicon project (see <http://wikipedia.org/wiki/Moby_Project>). It is a list of 113,809 official crosswords; that is, words that are considered valid in crossword puzzles and other word games. In the Moby collection, the filename is <span>113809of.fic</span>; you can download a copy, with the simpler name <span>words.txt</span>, from <http://thinkpython2.com/code/words.txt>.

Note: This step has already been done for you.

This file is in plain text, so you can open it with a text editor, but you can also read it from Python. The built-in function <span>open</span> takes the name of the file as a parameter and returns a <span>**file object**</span> you can use to read the file.

    >>> fin = open('words.txt')

<span>fin</span> is a common name for a file object used for input. The file object provides several methods for reading, including <span>readline</span>, which reads characters from the file until it gets to a newline and returns the result as a string:

    >>> fin.readline()
    'aa\n'

The first word in this particular list is “aa”, which is a kind of lava. The sequence `\n` represents the newline character that separates this word from the next.

The file object keeps track of where it is in the file, so if you call <span>readline</span> again, you get the next word:

    >>> fin.readline()
    'aah\n'

The next word is “aah”, which is a perfectly legitimate word, so stop looking at me like that. Or, if it’s the newline character that’s bothering you, we can get rid of it with the string method <span>strip</span>:

    >>> line = fin.readline()
    >>> word = line.strip()
    >>> word
    'aahed'

You can also use a file object as part of a <span>for</span> loop. This program reads <span>words.txt</span> and prints each word, one per line:

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        print(word)

