import pytest
import time
from pages.base_page import BasePage

class TestFlor2uAuth:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        page = browser.new_page()
        yield page
        time.sleep(1)
        if not page.is_closed():
            page.close()

    def test_successful_login(self, setup):
        page = setup
        base_page = BasePage(page)
        
        if not base_page.navigate("https://flor2u.ru/"):
            base_page.save_screenshot()
            pytest.fail("Не удалось загрузить сайт")

        try:
            base_page.click("//a[contains(text(),'Войти')]")
            base_page.fill("input[name='login']", "enzemalikova930@gmail.com")
            base_page.fill("input[name='password']", "wQx3yPR_WsJQbde")
            
            
            page.pause()  
            
            base_page.click("button._green")
            page.wait_for_url("https://flor2u.ru/personal/personal-data/", timeout=30000)
            
        except Exception as e:
            base_page.save_screenshot()
            pytest.fail(f"Тест упал: {str(e)}")