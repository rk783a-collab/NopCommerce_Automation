from playwright.sync_api import Page

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self,url:str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title

    def get_current_url(self):
        return self.page.current_url