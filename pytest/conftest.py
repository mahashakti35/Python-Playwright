import pytest


@pytest.fixture(scope="function")
def initial():
    print("initial Setup Done")
    return "pass"