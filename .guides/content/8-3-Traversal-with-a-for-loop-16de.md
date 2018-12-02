--------------------------------------

A lot of computations involve processing a string one character at a time. Often they start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a <span>**traversal**</span>. One way to write a traversal is with a <span>while</span> loop:

    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(letter)
        index = index + 1

This loop traverses the string and displays each letter on a line by itself. The loop condition is <span>index \< len(fruit)</span>, so when <span>index</span> is equal to the length of the string, the condition is false, and the body of the loop doesn’t run. The last character accessed is the one with the index <span>len(fruit)-1</span>, which is the last character in the string.

As an exercise, write a function that takes a string as an argument and displays the letters backward, one per line.

Another way to write a traversal is with a <span>for</span> loop:

    for letter in fruit:
        print(letter)

Each time through the loop, the next character in the string is assigned to the variable <span>letter</span>. The loop continues until no characters are left.

The following example shows how to use concatenation (string addition) and a <span>for</span> loop to generate an abecedarian series (that is, in alphabetical order). In Robert McCloskey’s book <span>*Make Way for Ducklings*</span>, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs these names in order:

    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        print(letter + suffix)

The output is:

    Jack
    Kack
    Lack
    Mack
    Nack
    Oack
    Pack
    Qack

Of course, that’s not quite right because “Ouack” and “Quack” are misspelled. As an exercise, modify the program to fix this error.

