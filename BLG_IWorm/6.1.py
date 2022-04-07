import requests
from bs4 import BeautifulSoup
import bs4

kv = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }

def get_HTML_Text(url):
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''
    
def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def print_univ_list(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
    
def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2021'
    html = get_HTML_Text(url)
    fill_univ_list(uinfo, html)
    print(uinfo,5)
    
main()