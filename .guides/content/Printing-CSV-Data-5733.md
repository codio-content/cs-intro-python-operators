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

## Unpacking 

In the code above, the variable `row` represents a list of data. The first element is the name of the player, the second element is the number of career home runs, and the third element states they are currently an active player. Python provides a way to take the descriptions of the each element and use it in the for loop.

![Unpacking CSV Info](.guides/images/unpacking-csv-info.png)

The for loop has three variables:`name`, `hr`, and `active`. The first variable, `name`, represents the first element in the list, the second variable, `hr`, represents the second element of the list, and the third variable, `active`, represents the third element. This is called unpacking.

```python
import csv

with open("home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    print(reader)
    next(reader) #skip the header names
    for name, hr, active in reader:
        print("{} hit {} home runs.".format(name, hr))
```

{try it}(python3 code/files/printing-csv.py 3)

|||challenge
## What happens if you:
* Remove `next(reader)` from the program?
* Remove the variable `active`?

|||

{try it}(python3 code/files/printing-csv.py 4)

<details><summary>**Unpacking and list length**</summary>Unpacking only works if you know how many elements are in the list. You must have the same number variables in the for loop as there are elements in the list. If you don't know how long a list is, you can always iterate over the list to access all of the elements.</details>

{Check It!|assessment}(multiple-choice-3850148086)
