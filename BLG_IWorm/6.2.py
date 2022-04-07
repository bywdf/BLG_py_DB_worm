import requests
from bs4 import BeautifulSoup
import bs4

url = 'https://www.shanghairanking.cn/rankings/bcur/2021'      # 大学排名的新网址
kv = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }

try:
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = 'utf-8'
    html =  r.text
except:
    pass

ulist = []
soup = BeautifulSoup(html, 'html.parser')
for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
        tds = tr('td')
        ulist.append([tds[0].string, tds[1].a.string, tds[4].string])  #大学排名的td顺序和视频中的有变化，且大学名字在<a>标签里面
      
for i in range(len(ulist)):
    for j in range(len(ulist[i])):
        ulist[i][j] = ulist[i][j].replace(' ','')
        ulist[i][j] = ulist[i][j].replace('\n','')   # 格式化列表，去掉多余的空格和回车
        
print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
for i in ulist:
        print("{:^10}\t{:^6}\t{:^10}".format(i[0],i[1],i[2]))


