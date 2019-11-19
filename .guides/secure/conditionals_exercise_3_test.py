import sys

student_work = open("code/selection/exercise3.py").read()
x = int(sys.argv[1])
exec(student_work)