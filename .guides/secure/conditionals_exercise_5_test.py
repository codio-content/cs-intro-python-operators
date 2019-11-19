import sys

student_work = open("code/selection/exercise5.py").read()
x = sys.argv[1]
exec(student_work)