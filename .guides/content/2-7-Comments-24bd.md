--------

As programs get bigger and more complicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why.

For this reason, it is a good idea to add notes to your programs to explain in natural language what the program is doing. These notes are called <span>**comments**</span>, and they start with the `#` symbol:

    # compute the percentage of the hour that has elapsed
    percentage = (minute * 100) / 60

In this case, the comment appears on a line by itself. You can also put comments at the end of a line:

    percentage = (minute * 100) / 60     # percentage of an hour

Everything from the <span>\#</span> to the end of the line is ignored—it has no effect on the execution of the program.

Comments are most useful when they document non-obvious features of the code. It is reasonable to assume that the reader can figure out <span>*what*</span> the code does; it is more useful to explain <span>*why*</span>.

This comment is redundant with the code and useless:

    v = 5     # assign 5 to v

This comment contains useful information that is not in the code:

    v = 5     # velocity in meters/second. 

Good variable names can reduce the need for comments, but long names can make complex expressions hard to read, so there is a tradeoff.

