url = 'https://jp.indeed.com/jobs'

base_url = 'https://jp.indeed.com'

url_search_china = 'https://jp.indeed.com/jobs?q=%E4%B8%AD%E5%9B%BD&vjk=6f8abd30348ed9d8'

keyword_search_list = [
    '外国',
    '中国',
    'ベトナム',
    'ネパール',
    'ミャンマー',
]

page_number = 5

headers = {
    'authority': 'jp.indeed.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': 'indeed_rcc=CTK; CTK=1hntpesakiefhban; _ga=GA1.2.126029954.1709323023; _gid=GA1.2.1432710750.1709323023; _gac_UA-90780-1=1.1709323023.CjwKCAiAloavBhBOEiwAbtAJO41DxVxacM9LLLjd95GFcyWp8vQMcQyqdXS9fzCytOoDW9Sk5Szk6BoCQGgQAvD_BwE; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtVHh_murgP_cZuCoPHTE0rE="; CF_BOTS-997=0; hpnode=1; _gcl_au=1.1.2056753744.1709335974; LC="co=JP"; LOCALE=ja; LOCALE=ja; CMP_VISITED=1; cmppmeta="eNoBSAC3/8j+Yv5W64nBqY8NgA8QYC2T6mqSaENwzdZ98SN3S1BXRsfLDn7fHH6oX7SxetYZiNr3r5NyQ4RAL0Ue8g+FJT0rTc61Fhq5UEm9Isg="; CSRF=WwKR23w3TuA2jFT8hZpliSombIYEdQgC; _cfuvid=UCmGKV7ZRLhH6jJ0y9MGD9CCcMjy_FBX_jAyZ_4cS6c-1709429641737-0.0.1.1-604800000; INDEED_CSRF_TOKEN=P7iICnZES4irP7uO7ST3J43LrM1498Xt; SURF=rpYAYUfOot2EfNewg9zXw8ZZYeLSnzHE; SHARED_INDEED_CSRF_TOKEN=P7iICnZES4irP7uO7ST3J43LrM1498Xt; MICRO_CONTENT_CSRF_TOKEN=ina8S7QY4PVUuKGVfSY1uVPuj1JpE3OF; cp=1; cp=2; ROJC=61ea90814187a63a:80c4dccce6d8264e:6aa27a2d0a8b01bd; LV="LA=1709434812:LV=1709429656:CV=1709434812:TS=1709335952"; RSJC=b644d415026357c0:51bf5a32803b9ed0:b59474e644c50a54:81dc42e2807e8681:3a5d3868062e9b40:424134925e15da04:e7f6e228c3093e0b:abb3b7656096e47b:ddadfcf76e3f2836:cc2831c2186fb4d7; PPID=eyJraWQiOiJkMzZkNmUzNi1lMWJlLTQzNzEtYjY0MS04MGZlZjM3YWQ4N2MiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJlODlhNTk0MTQ0MzIzMTI2IiwibGFzdF9hdXRoX3RpbWUiOjE3MDk0MzYyNjczMzcsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdXRoIjoiZ29vZ2xlIiwiY3JlYXRlZCI6MTcwOTI2NjgyNDAwMCwiaXNzIjoiaHR0cHM6Ly9zZWN1cmUuaW5kZWVkLmNvbSIsImxhc3RfYXV0aF9sZXZlbCI6IlNUUk9ORyIsImxvZ190cyI6MTcwOTQzNjI2NzMzNywiYXVkIjoiYzFhYjhmMDRmIiwicmVtX21lIjp0cnVlLCJleHAiOjE3MDk0MzgwNjcsImlhdCI6MTcwOTQzNjI2NywiZW1haWwiOiJiMTAyNDQ4NDk2NkBnbWFpbC5jb20ifQ.A9YioHEE9hF0ZU1XjYbsS8kQjvr9dbKtp2Fzkch7ZTcEFB-KGm6eoIeyKaBISFzUPluVrucaNcrLAAS-DeAr4w; SOCK="MUX9l2uo6M8WNAuKSgT_X_9tM08="; SHOE="Fr0HX6fU83v4mXYyjMwYNdORs1Y7YhlUvuCuc5s4EEij5jIpioK_fxY1dRJ-s6pxruVzlusXNeyrAAJOmDcZkpxvWb6D_CBrzML3MeRLglcWH1sLKavDrzqAuaBWo3Y1Gy2bxNk_NZCeykBu1pdJ7jt_iA=="; indeed_rcc="LV:CTK"; __cf_bm=.cQY0F54LHzSHdb6rmHgx1dHiLOxPKUr1H9jp2gxh0o-1709436632-1.0.1.1-goh5vvHUYBUTzH38IJN95VP8lh7fADj7EvDY6U_lwX9D0cLRoFhVQ2RY2uNFmLseEplPsWjcXR3YVy6w1MCs5w; __cf_bm=c8RHRa3gdd5_s_XDOLOQxidLGnT.jXQ9tBqNMcB0Sm0-1709436632-1.0.1.1-hzYgor1.JkjYwK1gniNunpbDYC8Gt2BRNwc2Nf0M8uNsN9CCXbvLGMDOZjCdperc3C8Ga8h8dZ1AkOyphaU.AQ; cf_clearance=LWDN6xIDyKJmLAb.7Iai_xGk7Oe4ZkWMAlKMljW0_0g-1709436654-1.0.1.1-UTMyy258HCDo3qs224evPqoorK4RwtIZzRdJPLOfi4F4BDzuAMMLDYAwdB4MZhYycPo7BmQcq2cH1sisJsxrOw; RQ="q=%E4%B8%AD%E5%9B%BD&l=&ts=1709436659057&pts=1709401944055:q=%E5%A4%96%E5%9B%BD&l=&ts=1709348867147&pts=1709344088475"; JSESSIONID=F0C51463CC69840F8B9C22947D725477; _gali=jobsearch-JapanPage; _dd_s=rum=2&id=8ef5262f-ac94-4032-8cae-63eaba923829&created=1709437365242&expire=1709438266655',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"122.0.6261.95"',
    'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.95", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.95"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

params = [
    {
        'q': '外国',
        'l': '',
        'from': 'searchOnSerp'
    },
    {
        'q': '中国',
        'l': '',
        'from': 'searchOnSerp'
    },
    {
        'q': 'ベトナム',
        'l': '',
        'from': 'searchOnSerp'
    },
    {
        'q': 'ベトナム',
        'l': '',
        'from': 'searchOnSerp'
    },
    {
        'q': 'ネパール',
        'l': '',
        'from': 'searchOnSerp'
    },
    {
        'q': 'ミャンマー',
        'l': '',
        'from': 'searchOnSerp'
    }
]

param_foreign = {
    'q': '外国',
    'l': '',
    'from': 'searchOnSerp'
}

param_china = {
    'q': '中国',
    'l': '',
    'from': 'HPRecent'
}

param_vietnam = {
    'q': 'ベトナム',
    'l': '',
    'from': 'searchOnSerp'
}

param_nepal = {
    'q': 'ネパール',
    'l': '',
    'from': 'searchOnSerp'
}

param_myanmar = {
    'q': 'ミャンマー',
    'l': '',
    'from': 'searchOnSerp'
}
