import sys

student_work = open("code/selection/exercise4.py").read()
x = sys.argv[1]
exec(student_work)