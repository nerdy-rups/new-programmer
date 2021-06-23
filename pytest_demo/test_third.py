import pytest


@pytest.mark.regression
def test_FifthTest():
    print ("This is a regression suite test case")

def test_sixthTest():
    print ("This is not in regression suite")

@pytest.mark.regression
def test_SeventhTest():
    print ("This is also a regression suite test case")

@pytest.mark.skip  # skip annotation is specific to mark test cases to be skipped
def test_EighthTest():
    assert "abc" == "def", "wtf!!"

@pytest.mark.xfail  # xfail annotation is specific to mark test cases which are to be run but should be skipped while displaying reports
def test_NinthTest():
    assert (1, 4, 6) < (0, 0, 0), "wtf!!"
