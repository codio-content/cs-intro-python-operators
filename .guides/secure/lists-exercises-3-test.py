import sys

student_work = open("code/lists/exercise3.py").read()

strings = sys.argv[1:]

#print(strings)
exec(student_work)