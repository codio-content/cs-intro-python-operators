---------------------

In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. <span>**Conditional statements**</span> give us this ability. The simplest form is the <span>if</span> statement:

    if x > 0:
        print('x is positive')

The boolean expression after <span>if</span> is called the <span>**condition**</span>. If it is true, the indented statement runs. If not, nothing happens.

<span>if</span> statements have the same structure as function definitions: a header followed by an indented body. Statements like this are called <span>**compound statements**</span>.

There is no limit on the number of statements that can appear in the body, but there has to be at least one. Occasionally, it is useful to have a body with no statements (usually as a place keeper for code you haven’t written yet). In that case, you can use the <span>pass</span> statement, which does nothing.

    if x < 0:
        pass          # TODO: need to handle negative values!

