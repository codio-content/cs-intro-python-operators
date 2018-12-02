-----------------------------------

In Python, most arithmetic operations are constant time; multiplication usually takes longer than addition and subtraction, and division takes even longer, but these run times don’t depend on the magnitude of the operands. Very large integers are an exception; in that case the run time increases with the number of digits.

Indexing operations—reading or writing elements in a sequence or dictionary—are also constant time, regardless of the size of the data structure.

A <span>for</span> loop that traverses a sequence or dictionary is usually linear, as long as all of the operations in the body of the loop are constant time. For example, adding up the elements of a list is linear:

        total = 0
        for x in t:
            total += x

The built-in function <span>sum</span> is also linear because it does the same thing, but it tends to be faster because it is a more efficient implementation; in the language of algorithmic analysis, it has a smaller leading coefficient.

As a rule of thumb, if the body of a loop is in $O(n^a)$ then the whole loop is in $O(n^{a+1})$. The exception is if you can show that the loop exits after a constant number of iterations. If a loop runs $k$ times regardless of $n$, then the loop is in $O(n^a)$, even for large $k$.

Multiplying by $k$ doesn’t change the order of growth, but neither does dividing. So if the body of a loop is in $O(n^a)$ and it runs $n/k$ times, the loop is in $O(n^{a+1})$, even for large $k$.

Most string and tuple operations are linear, except indexing and <span>len</span>, which are constant time. The built-in functions <span>min</span> and <span>max</span> are linear. The run-time of a slice operation is proportional to the length of the output, but independent of the size of the input.

String concatenation is linear; the run time depends on the sum of the lengths of the operands.

All string methods are linear, but if the lengths of the strings are bounded by a constant—for example, operations on single characters—they are considered constant time. The string method <span>join</span> is linear; the run time depends on the total length of the strings.

Most list methods are linear, but there are some exceptions:

-   Adding an element to the end of a list is constant time on average; when it runs out of room it occasionally gets copied to a bigger location, but the total time for $n$ operations is $O(n)$, so the average time for each operation is $O(1)$.

-   Removing an element from the end of a list is constant time.

-   Sorting is $O(n \log n)$.

Most dictionary operations and methods are constant time, but there are some exceptions:

-   The run time of <span>update</span> is proportional to the size of the dictionary passed as a parameter, not the dictionary being updated.

-   <span>keys</span>, <span>values</span> and <span>items</span> are constant time because they return iterators. But if you loop through the iterators, the loop will be linear.

The performance of dictionaries is one of the minor miracles of computer science. We will see how they work in Section [hashtable].

Read the Wikipedia page on sorting algorithms at <http://en.wikipedia.org/wiki/Sorting_algorithm> and answer the following questions:

1.  What is a “comparison sort?” What is the best worst-case order of growth for a comparison sort? What is the best worst-case order of growth for any sort algorithm?

2.  What is the order of growth of bubble sort, and why does Barack Obama think it is “the wrong way to go?”

3.  What is the order of growth of radix sort? What preconditions do we need to use it?

4.  What is a stable sort and why might it matter in practice?

5.  What is the worst sorting algorithm (that has a name)?

6.  What sort algorithm does the C library use? What sort algorithm does Python use? Are these algorithms stable? You might have to Google around to find these answers.

7.  Many of the non-comparison sorts are linear, so why does does Python use an $O(n \log n)$ comparison sort?

