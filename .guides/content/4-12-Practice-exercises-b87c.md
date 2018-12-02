---------

Use the following code file: </code/polygon.py>.

1.  Draw a stack diagram that shows the state of the program while executing <span>circle(bob, radius)</span>. You can do the arithmetic by hand or add <span>print</span> statements to the code.

{Try It}(sh .guides/bg.sh python3 code/polygon.py)

2.  The version of <span>arc</span> in Section [refactoring] is not very accurate because the linear approximation of the circle is always outside the true circle. As a result, the Turtle ends up a few pixels away from the correct destination. My solution shows a way to reduce the effect of this error. Read the code and see if it makes sense to you. If you draw a diagram, you might see how it works.

![image](/.guides/img/flowers.jpg)



3. Write an appropriately general set of functions that can draw flowers as in Figure .

Solution: <http://thinkpython2.com/code/flower.py>, also requires <http://thinkpython2.com/code/polygon.py>.

![image](/.guides/img/pies.jpg)

{Try It}(sh .guides/bg.sh python3 code/polygon.py)

4. Write an appropriately general set of functions that can draw shapes as in Figure .

Solution: <http://thinkpython2.com/code/pie.py>.

5. The letters of the alphabet can be constructed from a moderate number of basic elements, like vertical and horizontal lines and a few curves. Design an alphabet that can be drawn with a minimal number of basic elements and then write functions that draw the letters.

You should write one function for each letter, with names `draw_a`, `draw_b`, etc., and put your functions in a file named <span>letters.py</span>. You can download a “turtle typewriter” from <http://thinkpython2.com/code/typewriter.py> to help you test your code.

{Try It}(sh .guides/bg.sh python3 code/polygon.py)

You can get a solution from <http://thinkpython2.com/code/letters.py>; it also requires <http://thinkpython2.com/code/polygon.py>.

6. Read about spirals at <http://en.wikipedia.org/wiki/Spiral>; then write a program that draws an Archimedian spiral (or one of the other kinds). Solution: <http://thinkpython2.com/code/spiral.py>.

