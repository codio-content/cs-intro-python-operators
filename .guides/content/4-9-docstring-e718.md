---------

A <span>**docstring**</span> is a string at the beginning of a function that explains the interface (“doc” is short for “documentation”). Here is an example:

    def polyline(t, n, length, angle):
        """Draws n line segments with the given length and
        angle (in degrees) between them.  t is a turtle.
        """    
        for i in range(n):
            t.fd(length)
            t.lt(angle)

By convention, all docstrings are triple-quoted strings, also known as multiline strings because the triple quotes allow the string to span more than one line.

It is terse, but it contains the essential information someone would need to use this function. It explains concisely what the function does (without getting into the details of how it does it). It explains what effect each parameter has on the behavior of the function and what type each parameter should be (if it is not obvious).

Writing this kind of documentation is an important part of interface design. A well-designed interface should be simple to explain; if you have a hard time explaining one of your functions, maybe the interface could be improved.

