
import pytest


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture(scope="session")
def browserInstance(playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    yield page