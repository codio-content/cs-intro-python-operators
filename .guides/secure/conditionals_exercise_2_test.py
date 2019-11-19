import sys

student_work = open("code/selection/exercise2.py").read()
x = int(sys.argv[1])
exec(student_work)