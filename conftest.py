import pytest
from selene.support.shared import browser


@pytest.fixture
def size_of_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1500


@pytest.fixture
def open_website(size_of_browser):
    browser.open('https://demoqa.com/automation-practice-form')