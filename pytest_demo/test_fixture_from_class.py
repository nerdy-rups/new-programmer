import pytest

@pytest.mark.usefixtures("dataLoading")
class testingFixture():
    def trying_the_feature(self, dataLoading):
        print(dataLoading)
