------------

To choose a random word from the histogram, the simplest algorithm is to build a list with multiple copies of each word, according to the observed frequency, and then choose from the list:

    def random_word(h):
        t = []
        for word, freq in h.items():
            t.extend([word] * freq)

        return random.choice(t)

The expression <span>`[word] * freq`</span> creates a list with <span>freq</span> copies of the string <span>word</span>. The <span>extend</span> method is similar to <span>append</span> except that the argument is a sequence.

This algorithm works, but it is not very efficient; each time you choose a random word, it rebuilds the list, which is as big as the original book. An obvious improvement is to build the list once and then make multiple selections, but the list is still big.

An alternative is:

1.  Use <span>keys</span> to get a list of the words in the book.

2.  Build a list that contains the cumulative sum of the word frequencies (see Exercise in Chapter 10). The last item in this list is the total number of words in the book, $n$.

3.  Choose a random number from 1 to $n$. Use a bisection search (See Exercise in Chapter 10) to find the index where the random number would be inserted in the cumulative sum.

4.  Use the index to find the corresponding word in the word list.


Write a program that uses this algorithm to choose a random word from the book. 

{Try it}(python3 code/random_words.py)

Solution: <http://thinkpython2.com/code/analyze_book3.py>.

