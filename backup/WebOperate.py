import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebOperate:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)

    def click_next_page(self):
        next_page_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="pagination-page-next"]')
        next_page_button.click()
        time.sleep(3)

    def input_search_text(self, text):
        search_input = self.driver.find_element(By.ID, "text-input-what")
        search_input.clear()
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def get_html_source(self):
        return self.driver.page_source

