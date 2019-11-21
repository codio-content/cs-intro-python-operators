----------

## Writerow

Writing to a CSV file is similar to writing to a text file. Open the file and set the mode to write (`"w"`). If the file does not exist, Python will create it. Send content to the file with the method `writerow`. Like reading a CSV, you need to import the `csv` module. Instead of using a `reader`, you need to use a `writter` to write information to the file. When you read information from a CSV file, it is a list of strings. So information written to a CSV file should also be a list of strings.

```python
import csv
import os

path = "student_folder/csv"

with open(os.path.join(path,"write_practice.csv"), "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Greeting", "Language"])
    writer.writerow(["Hello", "English"])
    writer.writerow(["Bonjour", "French"])
    writer.writerow(["Hola", "Spanish"])
    writer.writerow(["Namaste", "Hindi"])
```

{try it}(python3 code/files/write_csv.py 1)
[Open the File](open_file student_folder/csv/write_practice.csv)

|||challenge
## What happens if you:
* Add a different delimiter: `csv.writer(output_file, delimiter="\t")`?
* Remove the last two lines of code and run it again?
* Change the mode to append `"a"` and run the program again?

|||

{try it}(python3 code/files/write_csv.py 2)
[Open the File](open_file student_folder/csv/write_practice.csv)

## Writerows

The `writerow` method writes only one row of information to a CSV file. The `writerows` method can write several rows of information to a CSV file. `writerows` takes either a list of strings (a single row of information) or a list of lists of strings (many rows of information).

![Writerows](.guides/images/writerows.png)

```python
import csv
import os

path = "student_folder/csv"

with open(os.path.join(path,"write_practice.csv"), "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerows([
      ["Artist", "Album", "Copies"],
      ["Michael Jackson", "Thriller", "47 million"],
      ["Eagles", "Their Greatest Hits 1971-1975", "38 million"],
      ["Eagles", "Hotel California", "26 million"]
    ])
```

{try it}(python3 code/files/write_csv.py 3)
[Open the File](open_file student_folder/csv/write_practice.csv)

|||challenge
## What happens if you:
* Change `writerows` to `writerow` and open the file?
* Change the mode to append `"a"` and run the program again?

|||

{try it}(python3 code/files/write_csv.py 4)
[Open the File](open_file student_folder/csv/write_practice.csv)

{Check It!|assessment}(fill-in-the-blanks-3611362990)

