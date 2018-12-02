-------------------

You can change the state of an object by making an assignment to one of its attributes. For example, to change the size of a rectangle without changing its position, you can modify the values of <span>width</span> and <span>height</span>:

    box.width = box.width + 50
    box.height = box.height + 100

You can also write functions that modify objects. For example, `grow_rectangle` takes a Rectangle object and two numbers, <span>dwidth</span> and <span>dheight</span>, and adds the numbers to the width and height of the rectangle:

    def grow_rectangle(rect, dwidth, dheight):
        rect.width += dwidth
        rect.height += dheight

Here is an example that demonstrates the effect:

    >>> box.width, box.height
    (150.0, 300.0)
    >>> grow_rectangle(box, 50, 100)
    >>> box.width, box.height
    (200.0, 400.0)

Inside the function, <span>rect</span> is an alias for <span>box</span>, so when the function modifies <span>rect</span>, <span>box</span> changes.

As an exercise, write a function named `move_rectangle` that takes a Rectangle and two numbers named <span>dx</span> and <span>dy</span>. It should change the location of the rectangle by adding <span>dx</span> to the <span>x</span> coordinate of <span>corner</span> and adding <span>dy</span> to the <span>y</span> coordinate of <span>corner</span>.

