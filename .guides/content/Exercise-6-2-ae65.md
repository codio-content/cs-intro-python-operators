------------

The Ackermann function, $A(m, n)$, is defined:

$$\begin{aligned}
A(m, n) = \begin{cases} 
              n+1 & \mbox{if } m = 0 \\ 
        A(m-1, 1) & \mbox{if } m > 0 \mbox{ and } n = 0 \\ 
A(m-1, A(m, n-1)) & \mbox{if } m > 0 \mbox{ and } n > 0.
\end{cases} \end{aligned}$$

See <http://en.wikipedia.org/wiki/Ackermann_function>. Write a function named <span>ack</span> that evaluates the Ackermann function. Use your function to evaluate <span>ack(3, 4)</span>, which should be 125. What happens for larger values of <span>m</span> and <span>n</span>? 

{Try It}(python3 code/exercises_4.py)

{Check It!|assessment}(code-output-compare-1992895610)
