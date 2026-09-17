import pytest

from constants import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture
def basepage(page):
    """Open SauceDemo before each test."""
    page.goto(BASE_URL)
    return page


@pytest.fixture
def login_page(basepage):
    """Return LoginPage object."""
    return LoginPage(basepage)