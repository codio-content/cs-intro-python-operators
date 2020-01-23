import os
import subprocess
import sys

path = "code/fundamentals"
file = "exercise5.py"
student_code = os.path.join(path, file)

def count_prints(file):
  num_prints = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if line.find("print") != -1:
        num_prints += 1
    
  return num_prints == 2

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "Okay, it is time to learn about operators.":
    return True
  else:
    return False

if count_prints(student_code):
  if check_output(student_code):
    print("<h2>Test passed!</h2>")
    sys.exit(0)
  else:
    print("<h2>Test did not pass</h2>")
    print("Program did not print 'Okay, it is time to learn about operators.'")
    sys.exit(1)
else:
  print("<h2>Test did not pass</h2>")
  print("Did not use two print statements.")
  sys.exit(1)
