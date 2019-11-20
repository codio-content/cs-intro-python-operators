----------

## Printing CSV Data

Previously, printing the contents of the CSV file would return lists of strings. This is not visually pleasing way of presenting the data. In the code below, `row` is a list. So you can reference each element with an index.

```python
import csv

with open("home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row[0], "\t\t", row[1], "\t\t", row[2])
```

<details><summary>**"\t\t"**</summary>Remember, the `\` character introduces escape characters (introduced in the strings unit). `\t` is the escape character means to insert a tab. `\t\t` means to print two tabs.</details>

{try it}(python3 code/files/printing-csv.py 1)

|||challenge
## What happens if you:
* Code suggestion
* Code suggestion

|||

{try it}(python3 code/path/to_file.py 2)

## Better Way to Print

Short introduction

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
