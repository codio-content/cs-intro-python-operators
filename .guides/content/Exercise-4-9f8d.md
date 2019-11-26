## Files Exercise 4

**Problem**
Write a program that reads a tab delimited CSV file and prints the name of the oldest person in the file.

**Expected Output**
The CSV file will look something like the one below. **Note**, there will be a row with header titles.

|Name |Age |Career|
|-----|:--:|------|
|Peter|38  |Doctor|
|Paul |41  |Lawyer|
|Mary |32  |Systems Engineer|

The first three lines of your code **must** look like this:

```python
import os, sys, csv

path = sys.argv[1]
file_name = sys.argv[2]
```
This allows for different text files and paths to be sent to your program for testing. The `TRY IT` button below will send a test file to your program. You should see the following output:

```text
The oldest person is Paul.
```

[Code Visualizer](open_tutor code/files/exercise4.py)
{try it}(python3 code/files/exercise4.py student_folder/.exercises test4.csv)

{Check It!|assessment}(code-output-compare-135786605)
