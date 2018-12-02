-----------

When I wrote <span>circle</span>, I was able to re-use <span>polygon</span> because a many-sided polygon is a good approximation of a circle. But <span>arc</span> is not as cooperative; we can’t use <span>polygon</span> or <span>circle</span> to draw an arc.

One alternative is to start with a copy of <span>polygon</span> and transform it into <span>arc</span>. The result might look like this:

    def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = angle / n
        
        for i in range(n):
            t.fd(step_length)
            t.lt(step_angle)

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

The second half of this function looks like <span>polygon</span>, but we can’t re-use <span>polygon</span> without changing the interface. We could generalize <span>polygon</span> to take an angle as a third argument, but then <span>polygon</span> would no longer be an appropriate name! Instead, let’s call the more general function <span>polyline</span>:

    def polyline(t, n, length, angle):
        for i in range(n):
            t.fd(length)
            t.lt(angle)

Now we can rewrite <span>polygon</span> and <span>arc</span> to use <span>polyline</span>:

    def polygon(t, n, length):
        angle = 360.0 / n
        polyline(t, n, length, angle)

    def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n
        polyline(t, n, step_length, step_angle)

{Try It}(sh .guides/bg.sh python3 code/turtle_world.py)

Finally, we can rewrite <span>circle</span> to use <span>arc</span>:

    def circle(t, r):
        arc(t, r, 360)

This process—rearranging a program to improve interfaces and facilitate code re-use—is called <span>**refactoring**</span>. In this case, we noticed that there was similar code in <span>arc</span> and <span>polygon</span>, so we “factored it out” into <span>polyline</span>.

If we had planned ahead, we might have written <span>polyline</span> first and avoided refactoring, but often you don’t know enough at the beginning of a project to design all the interfaces. Once you start coding, you understand the problem better. Sometimes refactoring is a sign that you have learned something.

