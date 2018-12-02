--------------------------------

Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly. In a computer program, repetition is also called <span>**iteration**</span>.

We have already seen two functions, <span>countdown</span> and `print_n`, that iterate using recursion. Because iteration is so common, Python provides language features to make it easier. One is the <span>for</span> statement we saw in Section 4.2. We’ll get back to that later.

Another is the <span>while</span> statement. Here is a version of <span>countdown</span> that uses a <span>while</span> statement:

    def countdown(n):
        while n > 0:
            print(n)
            n = n - 1
        print('Blastoff!')

You can almost read the <span>while</span> statement as if it were English. It means, “While <span>n</span> is greater than 0, display the value of <span>n</span> and then decrement <span>n</span>. When you get to 0, display the word <span>Blastoff!</span>”

More formally, here is the flow of execution for a <span>while</span> statement:

1.  Determine whether the condition is true or false.

2.  If false, exit the <span>while</span> statement and continue execution at the next statement.

3.  If the condition is true, run the body and then go back to step 1.

This type of flow is called a loop because the third step loops back around to the top.

The body of the loop should change the value of one or more variables so that the condition becomes false eventually and the loop terminates. Otherwise the loop will repeat forever, which is called an <span>**infinite loop**</span>. An endless source of amusement for computer scientists is the observation that the directions on shampoo, “Lather, rinse, repeat”, are an infinite loop.

In the case of <span>countdown</span>, we can prove that the loop terminates: if <span>n</span> is zero or negative, the loop never runs. Otherwise, <span>n</span> gets smaller each time through the loop, so eventually we have to get to 0.

For some other loops, it is not so easy to tell. For example:

    def sequence(n):
        while n != 1:
            print(n)
            if n % 2 == 0:        # n is even
                n = n / 2
            else:                 # n is odd
                n = n*3 + 1

The condition for this loop is <span>n != 1</span>, so the loop will continue until <span>n</span> is <span>1</span>, which makes the condition false.

Each time through the loop, the program outputs the value of <span>n</span> and then checks whether it is even or odd. If it is even, <span>n</span> is divided by 2. If it is odd, the value of <span>n</span> is replaced with <span>n\*3 + 1</span>. For example, if the argument passed to <span>sequence</span> is 3, the resulting values of <span>n</span> are 3, 10, 5, 16, 8, 4, 2, 1.

Since <span>n</span> sometimes increases and sometimes decreases, there is no obvious proof that <span>n</span> will ever reach 1, or that the program terminates. For some particular values of <span>n</span>, we can prove termination. For example, if the starting value is a power of two, <span>n</span> will be even every time through the loop until it reaches 1. The previous example ends with such a sequence, starting with 16.

The hard question is whether we can prove that this program terminates for <span>*all*</span> positive values of <span>n</span>. So far, no one has been able to prove it <span>*or*</span> disprove it! (See <http://en.wikipedia.org/wiki/Collatz_conjecture>.)

As an exercise, rewrite the function `print_n` from Section 5.8 using iteration instead of recursion.

