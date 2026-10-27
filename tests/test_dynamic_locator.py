import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.ui
def test_specific_product(logged_in_page):
    assert "inventory.html" in logged_in_page.url
    product =logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    expect(product).to_be_visible()

    product.get_by_role("button",name="Add to cart").click()
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

def test_next_specific_product(logged_in_page):
    assert "inventory.html" in logged_in_page.url
    next_product = logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Bike")
    expect(next_product).to_be_visible()
    next_product.get_by_role("button",name="Add to cart").click()
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")
