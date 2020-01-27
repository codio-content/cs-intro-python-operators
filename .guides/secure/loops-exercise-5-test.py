import os
import subprocess
import sys

path = "code/loops"
file = "exercise-5.py"
student_code = os.path.join(path, file)

def check_loops(file):
  loops = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "for" in line:
        loops += 1 
      if "while" in line:
        loops += 1 
  return loops == 2

def check_prints(file):
  prints = 0
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "print" in line:
        prints += 1  
  return prints == 2

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8")  == """....1
...2
..3
.4
5""":
    return True
  else:
    return False

if not check_loops(student_code):
  print("<h2>Test did not pass</h2>")
  print("A nested loop was not used")
  
if not check_prints(student_code):
  print("<h2>Test did not pass</h2>")
  print("Your program should have two print statements, one for each loop")
  
if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Your program did not produce the expected output")
  
if check_loops(student_code) and check_prints(student_code) and check_output(student_code):
  print("<h2>All tests passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)