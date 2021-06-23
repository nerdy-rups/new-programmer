"""Rule: Always put all code in one or the other function, where each function is treated as one test case.
And the function name should begin with "test". This is for the test runner and cmd to pick up"""

def test_firstTest():
    print("Hello! I am a pytest code..")

def test_SecondTest():
    print("Hello! I am also a pytest code..")
