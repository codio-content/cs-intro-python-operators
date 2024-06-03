import csv
import os

path = "student_folder/csv"

with open(os.path.join(path,"monty_python_movies.csv"), "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row)