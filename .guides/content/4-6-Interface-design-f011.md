----------------

The next step is to write <span>circle</span>, which takes a radius, <span>r</span>, as a parameter. Here is a simple solution that uses <span>polygon</span> to draw a 50-sided polygon:

    import math

    def circle(t, r):
        circumference = 2 * math.pi * r
        n = 50
        length = circumference / n
        polygon(t, n, length)

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

The first line computes the circumference of a circle with radius <span>r</span> using the formula $2 \pi r$. Since we use <span>math.pi</span>, we have to import <span>math</span>. By convention, <span>import</span> statements are usually at the beginning of the script.

<span>n</span> is the number of line segments in our approximation of a circle, so <span>length</span> is the length of each segment. Thus, <span>polygon</span> draws a 50-sided polygon that approximates a circle with radius <span>r</span>.

One limitation of this solution is that <span>n</span> is a constant, which means that for very big circles, the line segments are too long, and for small circles, we waste time drawing very small segments. One solution would be to generalize the function by taking <span>n</span> as a parameter. This would give the user (whoever calls <span>circle</span>) more control, but the interface would be less clean.

The <span>**interface**</span> of a function is a summary of how it is used: what are the parameters? What does the function do? And what is the return value? An interface is “clean” if it allows the caller to do what they want without dealing with unnecessary details.

In this example, <span>r</span> belongs in the interface because it specifies the circle to be drawn. <span>n</span> is less appropriate because it pertains to the details of <span>*how*</span> the circle should be rendered.

Rather than clutter up the interface, it is better to choose an appropriate value of <span>n</span> depending on <span>circumference</span>:

    def circle(t, r):
        circumference = 2 * math.pi * r
        n = int(circumference / 3) + 3
        length = circumference / n
        polygon(t, n, length)

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

Now the number of segments is an integer near <span>circumference/3</span>, so the length of each segment is approximately 3, which is small enough that the circles look good, but big enough to be efficient, and acceptable for any size circle.

Adding 3 to <span>n</span> guarantees that the polygon has at least 3 sides.

