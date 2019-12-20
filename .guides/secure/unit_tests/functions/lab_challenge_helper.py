import os, shutil

student_file = "/home/codio/workspace/code/functions/lab_challenge.py" # path to student file
new_location = "/home/codio/workspace/.guides/secure/unit_tests/functions" # new location for testing

shutil.copy(student_file, new_location) # copy student file to the new location
os.system("python3 .guides/secure/unit_tests/functions/lab_challenge_test.py") # run the unit test on student file