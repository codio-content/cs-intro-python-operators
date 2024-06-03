import os, shutil, sys

# path to student file
student_file = "/home/codio/workspace/code/functions/lab_challenge.py" 

# new location for testing
new_location = "/home/codio/workspace/.guides/secure/unit_tests/functions" 

# copy student file to the new location
shutil.copy(student_file, new_location)

# run the code test on student file
result = os.system("python3 .guides/secure/unit_tests/functions/lab_challenge_test.py") 

# Return the exit code to the Guide for the red "X" or green checkmark
if result == 0:
    sys.exit(0)
else:
    sys.exit(1)