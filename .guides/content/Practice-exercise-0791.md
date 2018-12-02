# Estimate pi

The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of $1 / \pi$:

$$\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} 
\sum^\infty_{k=0} \frac{(4k)!(1103+26390k)}{(k!)^4 396^{4k}}$$

Write a function called `estimate_pi` that uses this formula to compute and return an estimate of $\pi$. It should use a <span>while</span> loop to compute terms of the summation until the last term is smaller than <span>1e-15</span> (which is Python notation for $10^{-15}$). You can check the result by comparing it to <span>math.pi</span>.

{Try It}(python3 code/estimate_pi.py)

Solution: <http://thinkpython2.com/code/pi.py>.