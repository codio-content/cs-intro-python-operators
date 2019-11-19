----------

## Coding Sum
Python already has a `sum` function, but we are going to write some code that manually calculates the sum of a list. 

### Setup
We are going to need a variable `total` that will be the sum. Set `total` to 0. Create an empty list called `numbers`. We will want the list to be randomly generated numbers, so import the `random` library as well.

```python
import random

numbers = []
total = 0
```

### Random Numbers
Next, lets add 20 random integers (from 0 to 100) to the list `numbers` with a for loop.

```python
for i in range(20):
    numbers.append(random.randint(0, 100))
```

### List Iteration
Now that the list of random numbers is complete, write a for loop to iterate over the list. Remember to use `number` as the iteration variable because it is the singular of the list `numbers`. Add each element of the list the the `total` variable.

```python
for number in numbers:
    total += number
```

### Answer and Checking our Work
Once this loop has finished iterating over the list `numbers`, the variable `total` should represent the sum of the list. Use a `print` statement to see the value of `total`. We are also going to print the sum of `numbers` using the `sum` function to check our work. If the numbers match, our code is good.

```python
print("The sum of numbers is ", total)
print(sum(numbers))
```

<details><summary>**Code**</summary><img src=".guides/images/sum-list-code.png"/></details>

{try it}(python3 code/lists/lab-sum.py)

{Check It!|assessment}(multiple-choice-2639349764)
