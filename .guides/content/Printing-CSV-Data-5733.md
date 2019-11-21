----------

## Printing CSV Data

Previously, printing the contents of the CSV file would return lists of strings. This is not visually pleasing way of presenting the data. In the code below, `row` is a list. So you can reference each element with an index. This keeps Python from printing square brackets, quotation marks, etc. Instead, it prints just the contents of the CSV file.

```python
import csv

with open("home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row[0], "\t\t", row[1], "\t\t", row[2])
```

<details><summary>**"\t\t"**</summary>Remember, the `\` character introduces escape characters (see the strings unit). `\t` is the escape character means to insert a tab (blank space). `\t\t` means to print two tabs.</details>

{try it}(python3 code/files/printing-csv.py 1)

|||challenge
## What happens if you:
* Add a third `\t` in the print statement?
* Change the spacing in the print statement to `"\t\t|\t`?
* Add this line of code to the end of the program `print("----------------------------------------------------------")`?

|||

{try it}(python3 code/files/printing-csv.py 2)

## Better Way to Print

In the code above, the variable `row` represents a list of data. The first element is the name of the player, the second element is the number of career home runs, and the third element states they are currently an active player. Python provides a way to take the descriptions of the each element and use it in the for loop.

```python
Example code
```

{try it}(python3 code/path/to_file.py 3)

|||challenge
## What happens if you:
* Code suggestion
* Code suggestion

|||

{try it}(python3 code/path/to_file.py 4)

Insert reading question
