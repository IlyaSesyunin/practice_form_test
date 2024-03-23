import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.set_window_size(1900, 1000)

    yield

    browser.quit()
