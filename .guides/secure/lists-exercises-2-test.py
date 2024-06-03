import sys

student_work = open("code/lists/exercise2.py").read()

my_list = sys.argv[1:]

#print(my_list)
exec(student_work)