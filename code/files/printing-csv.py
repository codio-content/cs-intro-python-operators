import csv

with open("home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row[0], "\t\t", row[1], "\t\t", row[2])