import pytest

@pytest.fixture(scope="session")
def SecondInitial():
    print("Second initial Setup Done")
    yield
    print("end")

def test_initialtest(initial):
    print("initial test")
    assert initial == "pass"

def test_secondtest(SecondInitial):
    print("Second test")

@pytest.mark.skip
def test_thirdtest(SecondInitial):
    print("Third test")

@pytest.mark.smoke
def test_fourthTest(SecondInitial):
    print("Fourth test")