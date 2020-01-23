import os
import subprocess
import sys

path = "code/operators"
file = "exercise5.py"
student_code = os.path.join(path, file)

def check_code(file):
  has_string  = False
  has_float = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "3.0" in line:
        has_float = True
      if "'2'" in line or '"2"' in line:
        has_string = True
    
  return has_string and has_float

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "5":
    return True
  else:
    return False

if check_code(student_code):
  if check_output(student_code):
    print("<h2>Test passed!</h2>")
    sys.exit(0)
  else:
    print("<h2>Test did not pass</h2>")
    print("Program did not print '5'")
    sys.exit(1)
else:
  print("<h2>Test did not pass</h2>")
  print("Program does not have either a string or float variable")
  sys.exit(1)
