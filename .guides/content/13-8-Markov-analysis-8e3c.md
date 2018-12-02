---------------

If you choose words from the book at random, you can get a sense of the vocabulary, but you probably won’t get a sentence:

    this the small regard harriet which knightley's it most things

A series of random words seldom makes sense because there is no relationship between successive words. For example, in a real sentence you would expect an article like “the” to be followed by an adjective or a noun, and probably not a verb or adverb.

One way to measure these kinds of relationships is Markov analysis, which characterizes, for a given sequence of words, the probability of the words that might come next. For example, the song <span>*Eric, the Half a Bee*</span> begins:

> Half a bee, philosophically,\
> Must, ipso facto, half not be.\
> But half the bee has got to be\
> Vis a vis, its entity. D’you see?\
> \
> But can a bee be said to be\
> Or not to be an entire bee\
> When half the bee is not a bee\
> Due to some ancient injury?\

In this text, the phrase “half the” is always followed by the word “bee”, but the phrase “the bee” might be followed by either “has” or “is”.

The result of Markov analysis is a mapping from each prefix (like “half the” and “the bee”) to all possible suffixes (like “has” and “is”).

Given this mapping, you can generate a random text by starting with any prefix and choosing at random from the possible suffixes. Next, you can combine the end of the prefix and the new suffix to form the next prefix, and repeat.

For example, if you start with the prefix “Half a”, then the next word has to be “bee”, because the prefix only appears once in the text. The next prefix is “a bee”, so the next suffix might be “philosophically”, “be” or “due”.

In this example the length of the prefix is always two, but you can do Markov analysis with any prefix length.

Markov analysis:

1.  Write a program to read a text from a file and perform Markov analysis. The result should be a dictionary that maps from prefixes to a collection of possible suffixes. The collection might be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your program with prefix length two, but you should write the program in a way that makes it easy to try other lengths.

{Try it}(python3 code/markov_analysis.py)

2.  Add a function to the previous program to generate random text based on the Markov analysis. Here is an example from <span>*Emma*</span> with prefix length 2:

    > He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?“ ”I cannot make speeches, Emma:" he soon cut it all himself.

    For this example, I left the punctuation attached to the words. The result is almost syntactically correct, but not quite. Semantically, it almost makes sense, but not quite.

    What happens if you increase the prefix length? Does the random text make more sense?

3.  Once your program is working, you might want to try a mash-up: if you combine text from two or more books, the random text you generate will blend the vocabulary and phrases from the sources in interesting ways.

{Try it}(python3 code/markov_analysis.py)

Credit: This case study is based on an example from Kernighan and Pike, <span>*The Practice of Programming*</span>, Addison-Wesley, 1999.

You should attempt this exercise before you go on; then you can can download my solution from <http://thinkpython2.com/code/markov.py>. You will also need <http://thinkpython2.com/code/emma.txt>.

