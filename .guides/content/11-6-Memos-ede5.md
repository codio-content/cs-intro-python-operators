-----

If you played with the <span>fibonacci</span> function from Section 6.7, you might have noticed that the bigger the argument you provide, the longer the function takes to run. Furthermore, the run time increases quickly.

To understand why, consider the Figure below, which shows the <span>**call graph**</span> for <span>fibonacci</span> with <span>n=4</span>:

![image](/.guides/img/fibonacci.jpg)



A call graph shows a set of function frames, with lines connecting each frame to the frames of the functions it calls. At the top of the graph, <span>fibonacci</span> with <span>n=4</span> calls <span>fibonacci</span> with <span>n=3</span> and <span>n=2</span>. In turn, <span>fibonacci</span> with <span>n=3</span> calls <span>fibonacci</span> with <span>n=2</span> and <span>n=1</span>. And so on.

Count how many times <span>fibonacci(0)</span> and <span>fibonacci(1)</span> are called. This is an inefficient solution to the problem, and it gets worse as the argument gets bigger.

One solution is to keep track of values that have already been computed by storing them in a dictionary. A previously computed value that is stored for later use is called a <span>**memo**</span>. Here is a “memoized” version of <span>fibonacci</span>:

    known = {0:0, 1:1}

    def fibonacci(n):
        if n in known:
            return known[n]

        res = fibonacci(n-1) + fibonacci(n-2)
        known[n] = res
        return res

<span>`known`</span> is a dictionary that keeps track of the Fibonacci numbers we already know. It starts with two items: 0 maps to 0 and 1 maps to 1.

Whenever <span>fibonacci</span> is called, it checks <span>known</span>. If the result is already there, it can return immediately. Otherwise it has to compute the new value, add it to the dictionary, and return it.

If you run this version of <span>fibonacci</span> and compare it with the original, you will find that it is much faster.

