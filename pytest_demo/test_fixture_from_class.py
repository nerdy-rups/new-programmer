import pytest

@pytest.mark.usefixtures("dataLoading") #class names should begin
class TestingFixture(): #As per pytest rules, always use "Test(Capital T) in the class name"
    def test_the_feature(self, dataLoading):
        print(dataLoading)
        print(dataLoading[2])
