import os
import subprocess
import sys

path = "code/operators"
file = "lab-challenge.py"
student_code = os.path.join(path, file)
has_equality = False
has_less_than = False
has_greater_than = False
has_logical = False

def check_operators(file):
  logical_count = 0
  global has_equality
  global has_less_than
  global has_greater_than
  global has_logical
  
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if line.find("==") != -1 or line.find("!=") != -1:
        has_equality = True
      if line.find("<") != -1 or line.find("<=") != -1:
        has_less_than = True
      if line.find(">") != -1 or line.find(">=") != -1:
        has_greater_than = True
      if line.find("and") != -1:
        logical_count += 1
      if line.find("or") != -1:
        logical_count += 1
      if line.find("not") != -1:
        logical_count += 1
        
  if logical_count >= 2:
    has_logical = True
  
  return has_equality and has_less_than and has_greater_than and has_logical

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "False":
    print("<h2>Test passed!</h2>")
    sys.exit(0)

if check_operators(student_code):
  check_output(student_code)
else:
  print("<h2>Code didn't meet requirements</h2>")
  print("Equality: ", str(has_equality))
  print("Less Than: ", str(has_less_than))
  print("Greater Than: ", str(has_greater_than))
  print("Logical: ", str(has_logical))
  sys.exit(1)