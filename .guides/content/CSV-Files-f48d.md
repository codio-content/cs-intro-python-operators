----------

## CSV Files

Python can work with files besides just text files. Comma Separated Value (CSV) files are an example of a commonly used file format for storing data. CSV files are similar to a spreadsheet in that data is stored in rows and columns. Each row of data is on its own line in the file, and commas are used to indicate a new column. Here is an example of a CSV file.

![Monty Python CSV](.guides/images/monty-python-csv.png)

In order to read a CSV file, Python needs to import the `csv` module. If you are importing a module, always start your code with the import statements. The CSV file will be opened much like a text file, but Python needs to run the file through a CSV reader.

```python
import csv

with open("monty_python_movies.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row)
```

{try it}(python3 code/files/csv-basics.py 1)

|||challenge
## What happens if you:
* Remove the `import csv` line of code?
* Use the CSV filename as the parameter of `reader`:
```python
import csv

with open("monty_python_movies.csv", "r") as input_file:
    reader = csv.reader("monty_python_movies.csv")
    for row in reader:
        for data in row:
            print(data)
```

|||

{try it}(python3 code/files/csv-basics.py 2)

## Next

The first row of a CSV file is helpful because the header values provide context for the data. However, the first row is not useful if you want to know how many rows of data, or calculate the avg value, etc. The `next` command allows Python to skip the first row before looping through the CSV file.

```python
import csv

with open("home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader) #skip the header row
    for row in reader:
        print(row)
```

{try it}(python3 code/files/csv-basics.py 3)

|||challenge
## What happens if you:
* Remove the line `next(reader)`?
* Have two lines of `next(reader)`?

|||

{try it}(python3 code/files/csv-basics.py 4)

{Check It!|assessment}(multiple-choice-234456500)
