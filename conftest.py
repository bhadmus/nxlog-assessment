import pytest
from objects.page_actions import PageActions


@pytest.fixture
def actions(page):
    browser = PageActions(page)
    browser.launch_url()
    return browser
