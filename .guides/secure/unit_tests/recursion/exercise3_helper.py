import os, shutil, sys

# path to student file
student_file = "/home/codio/workspace/code/recursion/exercise3.py" 

# new location for testing
new_location = "/home/codio/workspace/.guides/secure/unit_tests/recursion" 

# copy student file to the new location
shutil.copy(student_file, new_location)

# run the code test on student file
result = os.system("python3 .guides/secure/unit_tests/recursion/exercise3_test.py") 

# Return the exit code to the Guide for the red "X" or green checkmark
if result == 0:
    sys.exit(0)
else:
    sys.exit(1)