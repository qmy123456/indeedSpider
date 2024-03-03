import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



from src.config import request_config

if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = webdriver.Chrome(options=chrome_options)

    chrome_driver.find_element(By.ID, "text-input-what")

    for keyword in request_config.keyword_search_list:
        search_input = chrome_driver.find_element(By.ID, "text-input-what")
        search_input.click()

        for _ in range(20):  # 假设输入框中的字符不会超过20个
            search_input.send_keys(Keys.BACK_SPACE)
        time.sleep(1)

        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

