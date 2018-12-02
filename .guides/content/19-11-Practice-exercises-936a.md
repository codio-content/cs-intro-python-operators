---------

The following is a function computes the binomial coefficient recursively.

    def binomial_coeff(n, k):
        """Compute the binomial coefficient "n choose k".

        n: number of trials
        k: number of successes

        returns: int
        """
        if k == 0:
            return 1
        if n == 0:
            return 0

        res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
        return res

Rewrite the body of the function using nested conditional expressions.

{Try It}(python3 code/binomial.py)

One note: this function is not very efficient because it ends up computing the same values over and over. You could make it more efficient by memoizing (see Section 11.6). But you will find that it’s harder to memoize if you write it using conditional expressions.

