'''
Requests库的爬取性能分析老师参与
尽管Requests库功能很友好、开发简单（其实除了import外只需一行主要代码），但其性能与专业爬虫相比还是有一定差距的。请编写一个小程序，“任意”找个url，测试一下成功爬取100次网页的时间。（某些网站对于连续爬取页面将采取屏蔽IP的策略，所以，要避开这类网站。）

请回复代码，并给出url及在自己机器上的运行时间。
'''

import requests
import time

kv = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }

def get_HTML_Text(url):
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()  # 如果不是200，引发HTTPError错误
        r.encoding = 'utf-8'
        return r.text
    except:
        return "产生异常"
        
if __name__ == '__main__':
    url = "http://www.zhihui.com"
    start = time.perf_counter()
    for i in range(100):
        get_HTML_Text(url)      
    end = time.perf_counter()
    spend = end - start
    print(spend)