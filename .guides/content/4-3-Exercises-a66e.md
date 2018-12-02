---------

The following is a series of exercises using TurtleWorld. They are meant to be fun, but they have a point, too. While you are working on them, think about what the point is.

The following sections have solutions to the exercises, so don’t look until you have finished (or at least tried).

1.  Write a function called <span>square</span> that takes a parameter named <span>t</span>, which is a turtle. It should use the turtle to draw a square.

    Write a function call that passes <span>bob</span> as an argument to <span>square</span>, and then run the program again.

2.  Add another parameter, named <span>length</span>, to <span>square</span>. Modify the body so length of the sides is <span>length</span>, and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for <span>length</span>.

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

3.  Make a copy of <span>square</span> and change the name to <span>polygon</span>. Add another parameter named <span>n</span> and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are $360/n$ degrees.

4.  Write a function called <span>circle</span> that takes a turtle, <span>t</span>, and radius, <span>r</span>, as parameters and that draws an approximate circle by calling <span>polygon</span> with an appropriate length and number of sides. Test your function with a range of values of <span>r</span>.

    Hint: figure out the circumference of the circle and make sure that <span>length \* n = circumference</span>.

5.  Make a more general version of <span>circle</span> called <span>arc</span> that takes an additional parameter <span>angle</span>, which determines what fraction of a circle to draw. <span>angle</span> is in units of degrees, so when <span>angle=360</span>, <span>arc</span> should draw a complete circle.

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)
