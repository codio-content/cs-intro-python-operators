###
If you have a <span>return</span> statement with a complex expression, you don’t have a chance to print the result before returning. Again, you can use a temporary variable. For example, instead of:

    return self.hands[i].removeMatches()

you could write:

    count = self.hands[i].removeMatches()
    return count

Now you have the opportunity to display the value of <span>count</span> before returning.

