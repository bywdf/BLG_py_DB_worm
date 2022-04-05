import requests

url = 'https://www.amazon.cn/Python%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E5%9F%BA%E7%A1%80-%E5%B5%A9%E5%A4%A9-%E7%A4%BC%E6%AC%A3-%E9%BB%84%E5%A4%A9%E7%BE%BD/dp/B06W9KM5P5/ref=sr_1_1?s=books&ie=UTF8&qid=1488437402&sr=1-1'
kv = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }

try:
    r = requests.get(url,timeout=30, headers=kv)
    r.raise_for_status()
    r.encoding = 'utf-8'
    print(r.text[:1000])
except:
    print('失败')