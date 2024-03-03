from bs4 import BeautifulSoup

from src.config import select_dom_config
from src.tool import beautifulsoup_tool

#读取一个本地的html文件
if __name__ == '__main__':

    file_path = '../res/testFile.html'
    # 以读取模式打开文件
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    a_tags = beautifulsoup_tool.find_deeply(soup, select_dom_config.left_page_path)
    for a in a_tags:
        print(a.get('aria-label'))
