###
Writing complex expressions is fine as long as they are readable, but they can be hard to debug. It is often a good idea to break a complex expression into a series of assignments to temporary variables.

For example:

    self.hands[i].addCard(self.hands[self.findNeighbor(i)].popCard())

This can be rewritten as:

    neighbor = self.findNeighbor(i)
    pickedCard = self.hands[neighbor].popCard()
    self.hands[i].addCard(pickedCard)

The explicit version is easier to read because the variable names provide additional documentation, and it is easier to debug because you can check the types of the intermediate variables and display their values.

Another problem that can occur with big expressions is that the order of evaluation may not be what you expect. For example, if you are translating the expression $\frac{x}{2 \pi}$ into Python, you might write:

    y = x / 2 * math.pi

That is not correct because multiplication and division have the same precedence and are evaluated from left to right. So this expression computes $x \pi / 2$.

A good way to debug expressions is to add parentheses to make the order of evaluation explicit:

     y = x / (2 * math.pi)

Whenever you are not sure of the order of evaluation, use parentheses. Not only will the program be correct (in the sense of doing what you intended), it will also be more readable for other people who haven’t memorized the order of operations.

