import sys

student_work = open("code/strings/lab-challenge.py").read()

s = sys.argv[1:]
my_string = ""

for char in s:
  my_string += char

exec(student_work)