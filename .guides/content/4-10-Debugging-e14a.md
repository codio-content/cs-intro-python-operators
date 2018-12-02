---------

An interface is like a contract between a function and a caller. The caller agrees to provide certain parameters and the function agrees to do certain work.

For example, <span>polyline</span> requires four arguments: <span>t</span> has to be a Turtle; <span>n</span> has to be an integer; <span>length</span> should be a positive number; and <span>angle</span> has to be a number, which is understood to be in degrees.

These requirements are called <span>**preconditions**</span> because they are supposed to be true before the function starts executing. Conversely, conditions at the end of the function are <span>**postconditions**</span>. Postconditions include the intended effect of the function (like drawing line segments) and any side effects (like moving the Turtle or making other changes).

Preconditions are the responsibility of the caller. If the caller violates a (properly documented!) precondition and the function doesn’t work correctly, the bug is in the caller, not the function.

If the preconditions are satisfied and the postconditions are not, the bug is in the function. If your pre- and postconditions are clear, they can help with debugging.

