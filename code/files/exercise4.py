import os, sys, csv

path = sys.argv[1]
file_name = sys.argv[2]
oldest_age = 0
oldest_name = ""

with open(os.path.join(path, file_name), "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    next(reader)
    for name, age, career in reader:
        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name
            
print("The oldest person is {}.".format(oldest_name))