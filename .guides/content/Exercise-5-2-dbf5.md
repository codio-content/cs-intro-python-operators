----------------

Fermat’s Last Theorem says that there are no positive integers $a$, $b$, and $c$ such that

   $$a^n + b^n = c^n$$ 

for any values of $n$ greater than 2.

1.  Write a function named `check_fermat` that takes four parameters—<span>a</span>, <span>b</span>, <span>c</span> and <span>n</span>—and checks to see if Fermat’s theorem holds. If $n$ is greater than 2 and

    $$a^n + b^n = c^n$$ the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

2.  Write a function that prompts the user to input values for <span>a</span>, <span>b</span>, <span>c</span> and <span>n</span>, converts them to integers, and uses `check_fermat` to check whether they violate Fermat’s theorem.

{Try It}(python3 code/exercise_5-2.py)

{Check It!|assessment}(code-output-compare-145839972)


