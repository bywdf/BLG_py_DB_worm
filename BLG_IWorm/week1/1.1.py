import requests

def get_HTML_Text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果不是200，引发HTTPError错误
        r.encoding = 'utf-8'
        return r.text
    except:
        return "产生异常"
        
if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(get_HTML_Text(url))
    
    
'''
kv = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }
'''