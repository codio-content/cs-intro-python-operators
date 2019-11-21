----------

## Delimiters

Delimiters are a predefined character that separates one piece of information from another. CSV files use commas as the delimiter by default. However, this makes the file hard to read for humans. It is possible to change the delimiter in Python ([click here](open_file data_with_tabs.csv) to see an example), but your code must reflect this change.

![Tab Delimiter](.guides/images/delimiter.png)

```python
import csv
import os

path = "student_folder/csv"

with open(os.path.join(path, "data_with_tabs.csv"), "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    for row in reader:
        print(row)
```

{try it}(python3 code/files/delimiters.py 1)

|||challenge
## What happens if you:
* Change the delimiter to `,`?
There is a slight difference when the delimiter is a tab and when it is a comma. With a tab delimiter, each row is a list of three strings. When the delimiter is a comma, each row is a list with a single string. Python cannot divide the data into the month, high temperature, and low temperature because it cannot find the delimiter. So it returns one, long string.

|||

{try it}(python3 code/files/delimiters.py 2)

{Check It!|assessment}(multiple-choice-2766230152)
