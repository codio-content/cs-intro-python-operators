----------

## Order of Operations

Python uses the PEMDAS method for determining order of operations.

![PEMDAS](.guides/images/pemdas.png)

The code below should output `7.0`.

```python
a = 2
b = 3
c = 4
result = 3 * a ** 3 / (b + 5) + c
print(result)
```

{try it}(python3 code/operators/playground-pemdas.py 1)

<details>
  <summary><b>Explanation</b></summary>
  <ul>
    <li>The first step is to compute <code>b + 5</code> (which is <code>8</code>) because it is surrounded by parentheses.</li>
    <li>Next, calculate <code>a ** 3</code> (which is <code>8</code>) because it is an exponent.</li>
    <li>Next, do the multiplication and division going from left to right. <code>3 * 8</code> is <code>24</code>.</li>
    <li>`24` divided by <code>8</code> is <code>3.0</code> (remember, the <code>/</code> operator returns a float).</li>
    <li>Finally, add <code>3.0</code> and <code>4</code> together to get <code>7.0</code>.</li>
  </ul>
</details>

|||challenge
## Mental Math
* `5 + 7 - 10 * 3 / 0.5`
<details>
  <summary>Solution</summary>
  <ul>
    <li><b>Step 1:</b> 10 * 3 = 30</li>
    <li><b>Step 2:</b> 30 / 0.5 = 60.0</li>
    <li><b>Step 3:</b> 7 - 60.0 = -53.0</li>
    <li><b>Step 4:</b> 5 + -53.0 = -48.0</li>
    <li><b>Solution:</b> -48.0</li>
  </ul>
</details><br>

* `(5 * 8) - 7 ** 2 - (-1 * 18)`

<details>
  <summary>Solution</summary>
  <ul>
    <li><b>Step 1:</b> 5 * 8 = 40</li>
    <li><b>Step 2:</b> -1 * 18 = -18</li>
    <li><b>Step 3:</b> 7 ** 2 = 49</li>
    <li><b>Step 4:</b> 40 - 49 = -9</li>
    <li><b>Step 5:</b> -9 - -18 = 9</li>
    <li><b>Solution:</b> 9</li>
  </ul>
</details><br>

* `9 / 3 + (100 ** 0.5) - 3`

<details>
  <summary>Solution</summary>
  <ul>
    <li><b>Step 1:</b> 100 ** 0.5 = 10</li>
    <li><b>Step 2:</b> 9 / 3 = 3.0</li>
    <li><b>Step 3:</b> 3.0 + 10 = 13.0</li>
    <li><b>Step 4:</b> 13.0 - 3 = 10.0</li>
    <li><b>Solution:</b> 10.0</li>
  </ul>
</details>

|||

{try it}(python3 code/operators/playground-pemdas.py 2)

{Check It!|assessment}(parsons-puzzle-3925273068)

