import pytest

@pytest.fixture(scope="session")
def app_url():
    url =  "https://www.saucedemo.com/"
    yield url
    print("\n Session Teardown")

@pytest.fixture
def logged_in_page(page,app_url):
    page.goto(app_url)
    page.locator('#user-name').fill("standard_user")
    page.locator('#password').fill("secret_sauce")
    page.locator('#login-button').click()

    yield page
