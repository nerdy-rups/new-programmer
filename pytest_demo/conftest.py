import pytest

@pytest.fixture(scope="class") # the scope will ensure that the fixture will be run only once for the whole class.
def dataLoading():
    print("data is being loaded")
    return ["Rupsha", "Ghosh", "my school", 565]
