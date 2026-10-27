from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_product_to_cart(self,product_name:str):
        product = self.page.locator(".inventory_item").filter(has_text=product_name)
        product.get_by_role("button",name="Add to cart").click()
