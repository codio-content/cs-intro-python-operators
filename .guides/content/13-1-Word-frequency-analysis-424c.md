-----------------------

As usual, you should at least attempt the exercises before you read my solutions.

1. Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.

   Hint: The <span>string</span> module provides a string named <span>`whitespace`</span>, which contains space, tab, newline, etc., and <span>`punctuation`</span> which contains the punctuation characters. Let’s see if we can make Python swear:

       >>> import string
       >>> string.punctuation
       '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

   Also, you might consider using the string methods <span>`strip`</span>, <span>`replace`</span> and <span>`translate`</span>.

{Try it}(python3 code/word_freq.py)

2. Go to Project Gutenberg (<http://gutenberg.org>) and download your favorite out-of-copyright book in plain text format.

   Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.

   Then modify the program to count the total number of words in the book, and the number of times each word is used.

   Print the number of different words used in the book. Compare different books by different authors, written in different eras. Which author uses the most extensive vocabulary?

3. Modify the program from the previous exercise to print the 20 most frequently used words in the book.

4. Modify the previous program to read a word list (see Section 9.1) and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that <span>*should*</span> be in the word list, and how many of them are really obscure?

{Try it}(python3 code/word_freq.py)