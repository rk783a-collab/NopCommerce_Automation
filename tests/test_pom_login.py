import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.smoke
@pytest.mark.ui
def test_complete_puchase(page, app_url):

    # Login page
    login_page = LoginPage(page)

    login_page.open(app_url)

    login_page.login("standard_user","secret_sauce")

    # Inventory page
    inventory_page = InventoryPage(page)

    expect(inventory_page.title).to_have_text("Products")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    expect(inventory_page.cart_badge).to_have_text("1")
    #cart
    cart_page = CartPage(page)
    cart_page.open_cart()
    product = cart_page.get_product("Sauce Labs Backpack")
    expect(product).to_be_visible()
    #Chec-Out
    cart_page.checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_details("Kumar","Tester","500001")
    checkout_page.continue_checkout()
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
    checkout_page.finish_order()

    #Order confirmation
    expect(checkout_page.confirmation_message).to_have_text("Thank you for your order!")