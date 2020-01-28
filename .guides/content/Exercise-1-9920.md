----------

## Lists Exercise 1

**Problem**
Write a program that takes a list of integers called `numbers` and replaces each element greater than 10 with a `'*'` (**Note** use single quotes, the auto-grader will not work with double quotes). Print the new version of `numbers`.

**Expected Output**
* If `numbers = [30, 1, 20, 4]` then you will print `['*', 1, '*', 4]`
* If `numbers = [5, 9, 11, 23]` then you will print `[5, 9, '*', '*']`

<details><summary>**Hint**</summary>Using the iteration variable alone is not sufficient to change the element of a list. You need to be able to access the **index** of the iteration variable to modify the element.</details>

**Important**
Do not edit the code in the top section. This code is necessary for the auto-grader to work. Add your code in the section below. Clicking the `TRY IT` button will test your code with `numbers = [30, 1, 20, 4]`.

<details><summary>**Where is the code visualizer?**</summary>Unfortunately, the code visualizer does not work with the statement `import sys`. Since importing the `sys` module is required for this problem, the code visualizer will not be available for this problem.</details>

{try it}(python3 code/lists/exercise1.py 30 1 20 4)

{Check It!|assessment}(code-output-compare-3095758084)
