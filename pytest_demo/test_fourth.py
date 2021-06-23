"""This file contains fixtures"""

import pytest

@pytest.fixture()
def initialSetup():
    print("setup fixture here! I will be executed first")
    yield # this is like a halt to the execution till the test cases that have this setup are complete. Whatever written after this will be executed after each TC.
    print("TC done. I will be executed last")

def test_TenthTest():
    print("From the fixtures file, but not a fixture related testcase")

def test_EleventhTest(initialSetup): # pass the name of the fixture method in the TC which want to use that setup
    print("I am a fixture testcase")

def test_TwelfthTest(initialSetup):
    print("I am also a fixture testcase")



