## Files Exercise 5

**Problem**
Write a program that reads a comma delimited CSV file and prints all of the cities which reside in the Southern Hemisphere. **Note**, any latitude with a negative value is south of the equator.

**Expected Output**
The CSV file will look something like the one below. **Note**, there will be a row with header titles.

|City |Country |Latitude |Longitude |
|-----|--------|:-------:|:--------:|
|Beijing|China|39|116
|Perth|Australia|-57|115|
|Port Moresby|Papua New Guinea|-25|147|
|Tokyo|Japan|35|139|

The first three lines of your code **must** look like this:

```python
import os, sys, csv

path = sys.argv[1]
file_name = sys.argv[2]
```
This allows for different text files and paths to be sent to your program for testing. The `TRY IT` button below will send a test file to your program. You should see the following output:

```text
The following cities are in the Southern Hemisphere: Perth, Port Moresby.
```

[Code Visualizer](open_tutor code/files/exercise5.py)
{try it}(python3 code/files/exercise5.py student_folder/.exercises test5.csv)

{Check It!|assessment}(code-output-compare-4037337142)
