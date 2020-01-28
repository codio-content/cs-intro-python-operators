import os
import subprocess
import sys

path = "code/operators"
file = "exercise3.py"
student_code = os.path.join(path, file)

def count_prints(file):
  num_prints = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if line.find("print") != -1:
        num_prints += 1
    
  return num_prints == 1

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "Hello world":
    return True
  else:
    return False
  
def count_variables(file):
  num_vars = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "=" in line:
        num_vars += 1
    
  return num_vars == 2

def no_empty_string(file):
  no_empty = True
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if '""' in line or "''" in line:
        no_empty = False
    
  return no_empty
  
if not count_variables(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use two variables.")

if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not print 'Hello world'.")

if not count_prints(student_code):
  print("<h2>Test did not pass</h2>")
  print("Did not use one print statement.")
  
if not no_empty_string(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program should not contain any empty strings.")

if check_output(student_code) and count_variables(student_code) and no_empty_string(student_code) and count_prints(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)