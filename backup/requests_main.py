import json
import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

from src.config import request_config

if __name__ == '__main__':
    # default_cookie = 'indeed_rcc=CTK; CTK=1hntpesakiefhban; _ga=GA1.2.126029954.1709323023; _gid=GA1.2.1432710750.1709323023; _gac_UA-90780-1=1.1709323023.CjwKCAiAloavBhBOEiwAbtAJO41DxVxacM9LLLjd95GFcyWp8vQMcQyqdXS9fzCytOoDW9Sk5Szk6BoCQGgQAvD_BwE; SURF=b1DfPwKmdUQkVbyRiZtmnnDkSGkiITdZ; _cfuvid=k1WHKTQr.OCHoa.STNRj7DYZxxaJ1qLHc4_bbnkr3FA-1709323024530-0.0.1.1-604800000; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtVHh_murgP_cZuCoPHTE0rE="; CSRF=SM4YfUcEgHi46veBE1HyTYKM0F6Cr0EE; CF_BOTS-997=0; INDEED_CSRF_TOKEN=CZ5fL0IsFU3owOiH4tOhZbztvEJiLaZn; hpnode=1; _gcl_au=1.1.2056753744.1709335974; LC="co=JP"; SHARED_INDEED_CSRF_TOKEN=CZ5fL0IsFU3owOiH4tOhZbztvEJiLaZn; LOCALE=ja; MICRO_CONTENT_CSRF_TOKEN=B20K1f01gFaPbBVAditq485aWUKwUVE1; PPID=""; LOCALE=ja; NOMOB=1; ROJC=6aa27a2d0a8b01bd; cmpsmeta="eNoBOADH//B5pfu8zsEQCVamgo1D60QEb47jgbdegvcoSYIVTveBEQSzWWWo61CcaQb6182qxkiHMv34Uh0cRT0crw=="; CMP_VISITED=1; cmppmeta="eNoBSAC3/8j+Yv5W64nBqY8NgA8QYC2T6mqSaENwzdZ98SN3S1BXRsfLDn7fHH6oX7SxetYZiNr3r5NyQ4RAL0Ue8g+FJT0rTc61Fhq5UEm9Isg="; RSJC=de0d9a61071722d7:b59474e644c50a54:09bee91fe13833e3:3846034a6a2a3ef1:cc2831c2186fb4d7:f2f881f075457efa:53b9000b68124f41:edd5aedeeda80c16; indeed_rcc="LV:CTK"; cf_clearance=oIXanwnkFwqLkLaOC1Zo03BTqQNltLRXEMDzQ6S_nGg-1709387921-1.0.1.1-kLEOfQa6fPV0hJ39rapr7ty.XHT4iGY6wRpGPeuOaN53z6rorj26kRBwtr_MEd47Sc7LP9Upj7aCXvUfHcVKkg; __cf_bm=PpprX9rfAAiNwpdR9vzKYZ6GuIu8D2uZwXPzzsCVRVw-1709389074-1.0.1.1-ti_ftODRBApDenhOaPqSCSEPFbBeU6Rr03kPUO0LjDYsF5W.3awt_gvxEcmi5A.0iO5Uc.ztfIEKKEzLHgSkjQ; LV="LA=1709389074:LV=1709385823:CV=1709389074:TS=1709335952"; RQ="q=%E4%B8%AD%E5%9B%BD&l=&ts=1709389361477&pts=1709381930074:q=%E5%A4%96%E5%9B%BD&l=&ts=1709348867147&pts=1709344088475"; JSESSIONID=379EE4AB964E9CBB037384FCCA18CA69; _gali=jobsearch-JapanPage; __cf_bm=.fYtxcAUadRLJBzFEHK0BZa_qp3qHtPTP7JN8Mu0yKQ-1709389793-1.0.1.1-F1z2Kj20JBIc9Jr7ih6ZR24DKSR_EXACqWPFDBjHJiq18OdSryBTlnC5mNPAnskIaoSlPXU_DPFeh5ii7OlWDA'

    # user_cookie = input("请输入Cookie: ")
    # if user_cookie:
    #     request_config.headers['Cookie'] = user_cookie
    # else:
    #     request_config.headers['Cookie'] = default_cookie

    # request_config.headers['Cookie'] = default_cookie
    response = requests.get(url=request_config.url_search_china, headers=request_config.headers)
    # response = requests.get(url=request_config.url_search_china, headers=request_config.headers)

    if response.ok:
        html_text = response.text
        pprint("访问成功:" + response.url)

        soup = BeautifulSoup(html_text, 'html.parser')
        # 遍历html标签
        # # 使用BeautifulSoup解析HTML

        # a_tags = beautifulsoup_tool.find_deeply(soup, select_dom_config.left_page_path)
        # for a in a_tags:
        #     a_title = a.get('aria-label')
        #     a_href = a.get('href')
        #     detail_page_url = request_config.base_url + a_href
        #     a_response = requests.get(url=detail_page_url, headers=request_config.headers)
        #     if a_response.ok:
        #         pprint(a_title + "访问成功")
        #         a_html = BeautifulSoup(a_response.text, 'html.parser')
        #         pprint(a_html.title)
        #     else:
        #         pprint(a_title + "访问失败:" + str(a_response.status_code))

        # 遍历js代码
        script_tag = soup.find('script', id='mosaic-data')
        data = re.findall('"results" : (.*?) },', script_tag)
        pprint(json.loads(data))

    else:
        pprint("访问失败 status_code:" + str(response.status_code))
