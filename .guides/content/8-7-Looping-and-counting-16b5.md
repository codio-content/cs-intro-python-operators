--------------------

The following program counts the number of times the letter <span>a</span> appears in a string:

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

This program demonstrates another pattern of computation called a <span>**counter**</span>. The variable <span>count</span> is initialized to 0 and then incremented each time an <span>a</span> is found. When the loop exits, <span>count</span> contains the result—the total number of <span>a</span>’s.

As an exercise, encapsulate this code in a function named <span>count</span>, and generalize it so that it accepts the string and the letter as arguments.

Then rewrite the function so that instead of traversing the string, it uses the three-parameter version of <span>find</span> from the previous section.

