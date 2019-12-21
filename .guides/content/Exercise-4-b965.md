----------

## Functions Exercise 4

**Problem**
Write a function called `best_team` that takes a file name and a file path as parameters. Read the comma-delimited CSV file specified by the file name and file path. The CSV file has a list of all of the MLB teams and their performance from the 2019 season. The function should return the team name for the team with the most wins. **Important**, the CSV file has a header of `Tm,Lg,G,W,L`, which stands for team name, league, games played, wins, and losses. Below are the file name and file path variables you will need for this exercise.

```python
file_name = "mlb_data.csv"
file_path = "student_folder/.exercises"
```

**Expected Output**
The function call should look like this, `best_team(file_name, file_path)`, and the function should return `HOU`. However, your function will be tested with other CSV files in which different teams will have the highest win total.

[Code Visualizer](open_tutor code/functions/exercise4.py)
{try it}(python3 code/functions/exercise4.py)

{Check It!|assessment}(test-3993992507)