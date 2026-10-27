import pytest
from playwright.sync_api import expect

def test_playwright_waits(logged_in_page):
    title = logged_in_page.locator(".title")
    title.wait_for(state="visible")
    expect(title).to_have_text("Products")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
