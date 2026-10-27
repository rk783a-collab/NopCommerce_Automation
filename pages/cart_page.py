from playwright.sync_api import Page

class CartPage():
    def __init__(self,page:Page):
        self.page = page

        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator("#checkout")
    def open_cart(self):
        self.cart_link.click()
    def get_product(self,product_name:str):
        return self.page.locator(".cart_item").filter(has_text=product_name)

    def checkout(self):
        self.checkout_button.click()
