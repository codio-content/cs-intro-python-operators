# Import student function form the newly copied file
from exercise5 import get_max

# Import system module
import sys

# Homemade unit test, call student function w/ instructor input & output
def test_student_code():
    """Homemade unit test for student work
    Return True if all of the tests pass
    Return False if at least one test fails"""
    
    # Boolean variables for each test
    test1 = False
    test2 = False
    test3 = False
    
    # Print title for visual feedback
    print("<h2>Testing your code...</h2>")
    
    # First test case
    if get_max([-5, -1, -2, -3, -4]) == -1:
        test1 = True
        print("Test 1 <b>passed</b>.")
    else:
        print("Test 1 did <b>not pass</b>.")
        
    # Second test case
    if get_max([10, 50, 33, 21, 77]) == 77:
        test2 = True
        print("Test 2 <b>passed</b>.")
    else:
        print("Test 2 did <b>not pass</b>.")
        
    # Third test case
    if get_max([2010, 111, 678, 0, 4]) == 2010:
        test3 = True
        print("Test 3 <b>passed</b>.")
    else:
        print("Test 3 did <b>not pass</b>.")
    
    # Return results of the unit tests
    print("<hr>")
    if test1 and test2 and test3:
        return True
    else:
        return False

# Print final results of the unit test
if test_student_code():
    print("<h3>All tests passed!</h3>")
    sys.exit(0)
else:
    print("<h3>Not all of the tests passed.</h3>")
    sys.exit(1)