-------------

The greatest common divisor (GCD) of $a$ and $b$ is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if $r$ is the remainder when $a$ is divided by $b$, then $gcd(a,
b) = gcd(b, r)$. As a base case, we can use $gcd(a, 0) = a$.

Write a function called `gcd` that takes parameters <span>a</span> and <span>b</span> and returns their greatest common divisor.

{Try it}(python3 code/gcd.py)

Credit: This exercise is based on an example from Abelson and Sussman’s <span>*Structure and Interpretation of Computer Programs*</span>.