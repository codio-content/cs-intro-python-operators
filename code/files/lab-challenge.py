import os

path = "student_folder/.labs"

with open(os.path.join(path, "myanmar.txt"), "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if "Burma" in line:
            line.replace("Burma", "Myanmar")
        
    print(lines, end="")