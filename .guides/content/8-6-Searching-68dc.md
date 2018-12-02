---------

What does the following function do?

    def find(word, letter):
        index = 0
        while index < len(word):
            if word[index] == letter:
                return index
            index = index + 1
        return -1

In a sense, <span>find</span> is the inverse of the operator. Instead of taking an index and extracting the corresponding character, it takes a character and finds the index where that character appears. If the character is not found, the function returns <span>-1</span>.

This is the first example we have seen of a <span>return</span> statement inside a loop. If <span>word[index] == letter</span>, the function breaks out of the loop and returns immediately.

If the character doesn’t appear in the string, the program exits the loop normally and returns <span>-1</span>.

This pattern of computation—traversing a sequence and returning when we find what we are looking for—is called a <span>**search**</span>.

As an exercise, modify <span>find</span> so that it has a third parameter, the index in <span>word</span> where it should start looking.

