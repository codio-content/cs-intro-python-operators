import sys

student_work = open("code/selection/lab_challenge.py").read()
month = int(sys.argv[1])
exec(student_work)