--------------------------------------

In Section 3.9, we used a stack diagram to represent the state of a program during a function call. The same kind of diagram can help interpret a recursive function.

Every time a function gets called, Python creates a frame to contain the function’s local variables and parameters. For a recursive function, there might be more than one frame on the stack at the same time.

The figure below shows a stack diagram for <span>countdown</span> called with <span>n = 3</span>.

![image](/.guides/img/stack2.jpg)



As usual, the top of the stack is the frame for `__main__`. It is empty because we did not create any variables in `__main__` or pass any arguments to it.

The four <span>countdown</span> frames have different values for the parameter <span>n</span>. The bottom of the stack, where <span>n=0</span>, is called the <span>**base case**</span>. It does not make a recursive call, so there are no more frames.

As an exercise, draw a stack diagram for `print_n` called with `s = 'Hello'` and <span>n=2</span>. Then write a function called `do_n` that takes a function object and a number, <span>n</span>, as arguments, and that calls the given function <span>n</span> times.

