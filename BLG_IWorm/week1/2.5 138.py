import requests

url = 'https://m.ip138.com/iplookup.asp?ip='
kv = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }
ip = '202.204.80.112'
try:
    r = requests.get(url+ip, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)[-500:]
    
except:
    print('失败')