
-------------

The first exercise asks you to put your square-drawing code into a function definition and then call the function, passing the turtle as a parameter. Here is a solution:

    def square(t):
        for i in range(4):
            t.fd(100)
            t.lt(90)

    square(bob)

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

The innermost statements, <span>fd</span> and <span>lt</span> are indented twice to show that they are inside the <span>for</span> loop, which is inside the function definition. The next line, <span>square(bob)</span>, is flush with the left margin, which indicates the end of both the <span>for</span> loop and the function definition.

Inside the function, <span>t</span> refers to the same turtle <span>bob</span>, so <span>t.lt(90)</span> has the same effect as <span>bob.lt(90)</span>. In that case, why not call the parameter <span>bob</span>? The idea is that <span>t</span> can be any turtle, not just <span>bob</span>, so you could create a second turtle and pass it as an argument to <span>square</span>:

    alice = turtle.Turtle()
    square(alice)

Wrapping a piece of code up in a function is called <span>**encapsulation**</span>. One of the benefits of encapsulation is that it attaches a name to the code, which serves as a kind of documentation. Another advantage is that if you re-use the code, it is more concise to call a function twice than to copy and paste the body!

