import pytest

@pytest.mark.regression
def test_ThirdTest():
    message = "Good morning"
    assert message == "Good Night", "Fail, strings not matching" # the 2nd string is printed when the assertion returns false

def test_FourthTest():
    a = 5
    b = 6
    assert (a+b) == 11, "Addition is wrong"

