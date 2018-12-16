-------------

The following exercises use the <span>turtle</span> module, described in Chapter 4:

Read the following function and see if you can figure out what it does (see the examples in Chapter 4). Then run it and see if you got it right.

    def draw(t, length, n):
        if n == 0:
            return
        angle = 50
        t.fd(length*n)
        t.lt(angle)
        draw(t, length, n-1)
        t.rt(2*angle)
        draw(t, length, n-1)
        t.lt(angle)
        t.bk(length*n)
