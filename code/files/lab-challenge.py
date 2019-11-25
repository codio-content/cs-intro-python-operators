import os

path = "student_folder/.labs"

with open(os.path.join(path, "myanmar.txt"), "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if "Burma" in line:
            print(line.replace("Burma", "Myanmar"))
        else:
            print(line)