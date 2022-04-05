import requests

url = 'http://www.so.com/s'
keywords = 'python'
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    kv = {'q': keywords}
    r = requests.get(url, params=kv, headers=headers)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = 'utf-8'
    print(len(r.text))
except:
    print('Error')