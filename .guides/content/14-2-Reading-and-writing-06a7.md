-------------------

A text file is a sequence of characters stored on a permanent medium like a hard drive, flash memory, or CD-ROM. We saw how to open and read a file in Section 9.1.

To write a file, you have to open it with mode `'w'` as a second parameter:

    >>> fout = open('output.txt', 'w')

If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn’t exist, a new one is created.

<span>`open`</span> returns a file object that provides methods for working with the file. The <span>`write`</span> method puts data into the file.

    >>> line1 = "This here's the wattle,\n"
    >>> fout.write(line1)
    24

The return value is the number of characters that were written. The file object keeps track of where it is, so if you call <span>write</span> again, it adds the new data to the end of the file.

    >>> line2 = "the emblem of our land.\n"
    >>> fout.write(line2)
    24

When you are done writing, you should close the file.

    >>> fout.close()

If you don’t close the file, it gets closed for you when the program ends.

