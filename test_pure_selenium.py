from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
driver = webdriver.Firefox()


class TestClass:

    def test_pure_selenium(self):
        driver.get("https://seleniumbase.io/demo_page")
        assert driver.title == 'Web Testing Page'
        
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 
            'tbody#tbodyId')))
        
        element = driver.find_element_by_xpath('//h1')
        assert element.text == 'Demo Page'
        
        driver.quit()

if __name__ == "__main__":
    test_pure_selenium(self)
