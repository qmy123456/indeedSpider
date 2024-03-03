import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from InviteInfo import InviteInfo
from src.config import select_dom_config, request_config
from src.tool import beautifulsoup_tool, csv_tool


def safe_soup_list(danger_list):
    if not danger_list:
        empty_soup = BeautifulSoup('暂无信息', 'html.parser')
        return [empty_soup]
    else:
        return danger_list


def get_one_page_info(a_soups):

    for a in a_soups:
        a_id = a.get('id')
        search_button = chrome_driver.find_element(By.ID, a_id)
        search_button.click()
        time.sleep(2)
        # 现在获取新的页面源代码
        new_html = chrome_driver.page_source
        new_soup = BeautifulSoup(new_html, 'html.parser')
        work_name = safe_soup_list(beautifulsoup_tool.find_deeply(new_soup, select_dom_config.work_name_path))

        job_detail = new_soup.find('div', class_='jobsearch-JobComponent-description')
        if not job_detail:
            time.sleep(2)
            job_detail = new_soup.find('div', class_='jobsearch-JobComponent-description')

        invite_info = InviteInfo()
        job_post = safe_soup_list(beautifulsoup_tool.find_deeply(job_detail, select_dom_config.job_post_path))
        # job_name
        invite_info.job_name = re.sub(r' - job post', '', work_name[0].text)
        print(re.sub(r' - job post', '', work_name[0].text))
        # job_post
        invite_info.job_post = job_post[0].text
        # company_link
        invite_info.company_link = a.get('href')

        job_type_list = job_detail.findAll('div', class_='css-29lcrl eu4oa1w0')

        for job_type in job_type_list:
            if job_type.text == '企業名':
                next_div = job_type.find_next_sibling('div')
                # company_name
                invite_info.company_name = next_div.text

            if job_type.text == '本社所在地':
                next_div = job_type.find_next_sibling('div')
                # company_address
                invite_info.company_address = next_div.text

            if job_type.text == '代表電話番号':
                next_div = job_type.find_next_sibling('div')
                # tanto_name
                invite_info.tanto_phone = next_div.text

            if job_type.text == '代表者名':
                next_div = job_type.find_next_sibling('div')
                # tanto_phone
                invite_info.tanto_name = next_div.text

        page_info_list.append(invite_info)


def click_next_page():
    next_page_button = chrome_driver.find_element(By.CSS_SELECTOR, '[data-testid="pagination-page-next"]')
    next_page_button.click()
    time.sleep(3)


def input_search_text(text):
    search_input = chrome_driver.find_element(By.ID, "text-input-what")
    search_input.click()
    for _ in range(20):  # 假设输入框中的字符不会超过20个
        search_input.send_keys(Keys.BACK_SPACE)
    time.sleep(1)

    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)


if __name__ == '__main__':
    page_info_list = []

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = webdriver.Chrome(options=chrome_options)

    for keyword in request_config.keyword_search_list:
        print(keyword + '开始:')
        input_search_text(keyword)

        for i in range(request_config.page_number):
            print(f"{keyword}:第{str(i+1)}页")
            # 获取页面的HTML源代码
            page_html = chrome_driver.page_source
            soup = BeautifulSoup(page_html, 'html.parser')
            # 遍历html标签 使用BeautifulSoup解析HTML
            a_tags = beautifulsoup_tool.find_deeply(soup, select_dom_config.left_page_path)
            get_one_page_info(a_tags)
            click_next_page()

    # 去重
    invites_unique = csv_tool.remove_duplicates(page_info_list)
    # 输出到CSV
    csv_tool.invites_to_csv(invites_unique, '../output/result.csv')
