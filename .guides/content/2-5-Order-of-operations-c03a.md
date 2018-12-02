-------------------

When an expression contains more than one operator, the order of evaluation depends on the <span>**order of operations**</span>. For mathematical operators, Python follows mathematical convention. The acronym <span>**PEMDAS**</span> is a useful way to remember the rules:

-   <span>**P**</span>arentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, <span>2 \* (3-1)</span> is 4, and <span>(1+1)\*\*(5-2)</span> is 8. You can also use parentheses to make an expression easier to read, as in <span>(minute \* 100) / 60</span>, even if it doesn’t change the result.

-   <span>**E**</span>xponentiation has the next highest precedence, so <span>1 + 2\*\*3</span> is 9, not 27, and <span>2 \* 3\*\*2</span> is 18, not 36.

-   <span>**M**</span>ultiplication and <span>**D**</span>ivision have higher precedence than <span>**A**</span>ddition and <span>**S**</span>ubtraction. So <span>2\*3-1</span> is 5, not 4, and <span>6+4/2</span> is 8, not 5.

-   Operators with the same precedence are evaluated from left to right (except exponentiation). So in the expression <span>degrees / 2 \* pi</span>, the division happens first and the result is multiplied by <span>pi</span>. To divide by $2 \pi$, you can use parentheses or write <span>degrees / 2 / pi</span>.

I don’t work very hard to remember the precedence of operators. If I can’t tell by looking at the expression, I use parentheses to make it obvious.

