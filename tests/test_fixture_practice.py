import pytest
from playwright.sync_api import expect
def test_inventory_page(logged_in_page):

    assert "inventory.html" in logged_in_page.url

def test_products_visible(logged_in_page):
    assert logged_in_page.locator(".title").is_visible()

    # title = logged_in_page.locator(".title")
    #
    # expect(title).to_have_text("Products")













