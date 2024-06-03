import sys

student_work = open("code/lists/exercise5.py").read()

numbers = sys.argv[1:]

for i in range(len(numbers)):
  numbers[i] = int(numbers[i])

#print(numbers)
exec(student_work)