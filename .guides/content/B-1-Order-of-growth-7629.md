---------------

Suppose you have analyzed two algorithms and expressed their run times in terms of the size of the input: Algorithm A takes $100n+1$ steps to solve a problem with size $n$; Algorithm B takes $n^2 + n + 1$ steps.

The following table shows the run time of these algorithms for different problem sizes:

  -------- ------------- -------------
     Input   Run time of   Run time of
      size   Algorithm A   Algorithm B
        10         1 001           111
       100        10 001        10 101
     1 000       100 001     1 001 001
    10 000     1 000 001   $> 10^{10}$
  -------- ------------- -------------

At $n=10$, Algorithm A looks pretty bad; it takes almost 10 times longer than Algorithm B. But for $n=100$ they are about the same, and for larger values A is much better.

The fundamental reason is that for large values of $n$, any function that contains an $n^2$ term will grow faster than a function whose leading term is $n$. The <span>**leading term**</span> is the term with the highest exponent.

For Algorithm A, the leading term has a large coefficient, 100, which is why B does better than A for small $n$. But regardless of the coefficients, there will always be some value of $n$ where $a n^2 > b n$, for any values of $a$ and $b$.

The same argument applies to the non-leading terms. Even if the run time of Algorithm A were $n+1000000$, it would still be better than Algorithm B for sufficiently large $n$.

In general, we expect an algorithm with a smaller leading term to be a better algorithm for large problems, but for smaller problems, there may be a <span>**crossover point**</span> where another algorithm is better. The location of the crossover point depends on the details of the algorithms, the inputs, and the hardware, so it is usually ignored for purposes of algorithmic analysis. But that doesn’t mean you can forget about it.

If two algorithms have the same leading order term, it is hard to say which is better; again, the answer depends on the details. So for algorithmic analysis, functions with the same leading term are considered equivalent, even if they have different coefficients.

An <span>**order of growth**</span> is a set of functions whose growth behavior is considered equivalent. For example, $2n$, $100n$ and $n+1$ belong to the same order of growth, which is written $O(n)$ in <span>**Big-Oh notation**</span> and often called <span>**linear**</span> because every function in the set grows linearly with $n$.

All functions with the leading term $n^2$ belong to $O(n^2)$; they are called <span>**quadratic**</span>.

The following table shows some of the orders of growth that appear most commonly in algorithmic analysis, in increasing order of badness.

![.guides/img/bTable](.guides/img/bTable.jpg)

For the logarithmic terms, the base of the logarithm doesn’t matter; changing bases is the equivalent of multiplying by a constant, which doesn’t change the order of growth. Similarly, all exponential functions belong to the same order of growth regardless of the base of the exponent. Exponential functions grow very quickly, so exponential algorithms are only useful for small problems.

Read the Wikipedia page on Big-Oh notation at <http://en.wikipedia.org/wiki/Big_O_notation> and answer the following questions:

1.  What is the order of growth of $n^3 + n^2$? What about $1000000 n^3 + n^2$? What about $n^3 + 1000000 n^2$?

2.  What is the order of growth of $(n^2 + n) \cdot (n + 1)$? Before you start multiplying, remember that you only need the leading term.

3.  If $f$ is in $O(g)$, for some unspecified function $g$, what can we say about $af+b$?

4.  If $f_1$ and $f_2$ are in $O(g)$, what can we say about $f_1 + f_2$?

5.  If $f_1$ is in $O(g)$ and $f_2$ is in $O(h)$, what can we say about $f_1 + f_2$?

6.  If $f_1$ is in $O(g)$ and $f_2$ is $O(h)$, what can we say about $f_1 \cdot f_2$?

Programmers who care about performance often find this kind of analysis hard to swallow. They have a point: sometimes the coefficients and the non-leading terms make a real difference. Sometimes the details of the hardware, the programming language, and the characteristics of the input make a big difference. And for small problems asymptotic behavior is irrelevant.

But if you keep those caveats in mind, algorithmic analysis is a useful tool. At least for large problems, the “better” algorithm is usually better, and sometimes it is <span>*much*</span> better. The difference between two algorithms with the same order of growth is usually a constant factor, but the difference between a good algorithm and a bad algorithm is unbounded!

