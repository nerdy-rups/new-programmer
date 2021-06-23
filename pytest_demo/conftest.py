import pytest

@pytest.fixture(scope="class")
def dataLoading():
    print("data is being loaded")
    return ["Rupsha", "Ghosh", "Female", 26]
