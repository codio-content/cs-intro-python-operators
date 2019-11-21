import os

path = "student_folder/text"

output_file = open(os.path.join(path, "practice1.txt"), "w")
print(output_file)