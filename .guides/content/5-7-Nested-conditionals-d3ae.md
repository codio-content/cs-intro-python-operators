-------------------

One conditional can also be nested within another. We could have written the example in the previous section like this:

    if x == y:
        print('x and y are equal')
    else:
        if x < y:
            print('x is less than y')
        else:
            print('x is greater than y')

The outer conditional contains two branches. The first branch contains a simple statement. The second branch contains another <span>if</span> statement, which has two branches of its own. Those two branches are both simple statements, although they could have been conditional statements as well.

Although the indentation of the statements makes the structure apparent, <span>**nested conditionals**</span> become difficult to read very quickly. It is a good idea to avoid them when you can.

Logical operators often provide a way to simplify nested conditional statements. For example, we can rewrite the following code using a single conditional:

    if 0 < x:
        if x < 10:
            print('x is a positive single-digit number.')

The <span>print</span> statement runs only if we make it past both conditionals, so we can get the same effect with the <span>and</span> operator:

    if 0 < x and x < 10:
        print('x is a positive single-digit number.')

For this kind of condition, Python provides a more concise option:

    if 0 < x < 10:
        print('x is a positive single-digit number.')

