==============================

> This appendix is an edited excerpt from <span>*Think Complexity*</span>, by Allen B. Downey, also published by O’Reilly Media (2012). When you are done with this book, you might want to move on to that one.

<span>**Analysis of algorithms**</span> is a branch of computer science that studies the performance of algorithms, especially their run time and space requirements. See <http://en.wikipedia.org/wiki/Analysis_of_algorithms>.

The practical goal of algorithm analysis is to predict the performance of different algorithms in order to guide design decisions.

During the 2008 United States Presidential Campaign, candidate Barack Obama was asked to perform an impromptu analysis when he visited Google. Chief executive Eric Schmidt jokingly asked him for “the most efficient way to sort a million 32-bit integers.” Obama had apparently been tipped off, because he quickly replied, “I think the bubble sort would be the wrong way to go.” See <http://www.youtube.com/watch?v=k4RRi_ntQc8>.

This is true: bubble sort is conceptually simple but slow for large datasets. The answer Schmidt was probably looking for is “radix sort” (<http://en.wikipedia.org/wiki/Radix_sort>)[^2].

The goal of algorithm analysis is to make meaningful comparisons between algorithms, but there are some problems:

-   The relative performance of the algorithms might depend on characteristics of the hardware, so one algorithm might be faster on Machine A, another on Machine B. The general solution to this problem is to specify a <span>**machine model**</span> and analyze the number of steps, or operations, an algorithm requires under a given model.

-   Relative performance might depend on the details of the dataset. For example, some sorting algorithms run faster if the data are already partially sorted; other algorithms run slower in this case. A common way to avoid this problem is to analyze the <span>**worst case**</span> scenario. It is sometimes useful to analyze average case performance, but that’s usually harder, and it might not be obvious what set of cases to average over.

-   Relative performance also depends on the size of the problem. A sorting algorithm that is fast for small lists might be slow for long lists. The usual solution to this problem is to express run time (or number of operations) as a function of problem size, and group functions into categories depending on how quickly they grow as problem size increases.

The good thing about this kind of comparison is that it lends itself to simple classification of algorithms. For example, if I know that the run time of Algorithm A tends to be proportional to the size of the input, $n$, and Algorithm B tends to be proportional to $n^2$, then I expect A to be faster than B, at least for large values of $n$.

This kind of analysis comes with some caveats, but we’ll get to that later.

