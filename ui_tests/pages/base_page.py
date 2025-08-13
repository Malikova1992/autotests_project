from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(60000)

    def navigate(self, url: str):
        try:
            self.page.goto(url, timeout=60000, wait_until="domcontentloaded")
            return True
        except:
            return False

    def click(self, selector: str):
        self.page.wait_for_selector(selector, state="visible", timeout=30000)
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.wait_for_selector(selector, state="visible", timeout=30000)
        self.page.fill(selector, text)

    def save_screenshot(self):
        try:
            self.page.screenshot(path="error.png", full_page=True)
            return True
        except:
            return False