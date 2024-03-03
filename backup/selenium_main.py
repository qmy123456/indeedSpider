from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.config import request_config
from src.config import select_dom_config
from src.tool import beautifulsoup_tool

if __name__ == '__main__':
    # 设置Chrome选项，可以在这里添加更多的行为，例如无头模式等。
    chrome_options = Options()
    # 初始化WebDriver
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # 打开网页
    chrome_driver.get(request_config.url_search_china)

    # # window.mosaic.initialData.publicMetadata.mosaicProviderJobCardsModel.results
    # search_china_result = chrome_driver.execute_script(
    #     "return (function(){return window.mosaic.initialData.publicMetadata.mosaicProviderJobCardsModel.results;})();")
    # job_data_list = []
    # for item in search_china_result:
    #     obj = {
    #         'company': item.get('company', ''),
    #     }
    #     job_data_list.append(obj)
    #
    # # 打印数据
    # print(job_data_list)

    # 获取页面的HTML源代码
    page_html = chrome_driver.page_source
    soup = BeautifulSoup(page_html, 'html.parser')
    # 遍历html标签 使用BeautifulSoup解析HTML
    a_tags = beautifulsoup_tool.find_deeply(soup, select_dom_config.left_page_path)
    for a in a_tags:
        a_id = a.get('id')
        search_button = chrome_driver.find_element(By.ID, a_id)
        search_button.click()



    # 关闭浏览器
    chrome_driver.quit()
