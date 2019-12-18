import os, shutil

f = "code/functions/lab_challenge.py"
shutil.copy(f, ".guides/secure/unit_tests/functions")
os.system("python3 -m unittest")