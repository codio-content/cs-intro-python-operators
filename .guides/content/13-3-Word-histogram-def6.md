--------------

You should attempt the previous exercises before you go on. You can download my solution from <http://thinkpython2.com/code/analyze_book1.py>. You will also need <http://thinkpython2.com/code/emma.txt>.

Here is a program that reads a file and builds a histogram of the words in the file:

    import string

    def process_file(filename):
        hist = dict()
        fp = open(filename)
        for line in fp:
            process_line(line, hist)
        return hist

    def process_line(line, hist):
        line = line.replace('-', ' ')
        
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    hist = process_file('emma.txt')

This program reads <span>emma.txt</span>, which contains the text of <span>*Emma*</span> by Jane Austen.

`process_file` loops through the lines of the file, passing them one at a time to `process_line`. The histogram <span>hist</span> is being used as an accumulator.

`process_line` uses the string method <span>replace</span> to replace hyphens with spaces before using <span>split</span> to break the line into a list of strings. It traverses the list of words and uses <span>strip</span> and <span>lower</span> to remove punctuation and convert to lower case. (It is a shorthand to say that strings are “converted”; remember that strings are immutable, so methods like <span>strip</span> and <span>lower</span> return new strings.)

Finally, `process_line` updates the histogram by creating a new item or incrementing an existing one.

To count the total number of words in the file, we can add up the frequencies in the histogram:

    def total_words(hist):
        return sum(hist.values())

The number of different words is just the number of items in the dictionary:

    def different_words(hist):
        return len(hist)

Here is some code to print the results:

    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

And the results:

    Total number of words: 161080
    Number of different words: 7214

