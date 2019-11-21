import csv

with open("home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)
    for name, hr, active in reader:
        print(f"{name} hit {hr} home runs.")