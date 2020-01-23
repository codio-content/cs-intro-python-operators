import os
import subprocess
import sys

path = "code/operators"
file = "exercise4.py"
student_code = os.path.join(path, file)

def check_code(file):
  has_seven  = False
  has_two = False
  has_div = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "7" in line:
        has_seven = True
      if "2" in line:
        has_two = True
      if "/" in line or "//" in line:
        has_div = True
    
  return has_seven and has_two and has_div

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "3":
    return True
  else:
    return False

if check_code(student_code):
  if check_output(student_code):
    print("<h2>Test passed!</h2>")
    sys.exit(0)
  else:
    print("<h2>Test did not pass</h2>")
    print("Program did not print '3'")
    sys.exit(1)
else:
  print("<h2>Test did not pass</h2>")
  print("7 was not divided by 2")
  sys.exit(1)
