import requests

url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'}
cookies = {
    'Cookie':'session-id=460-1384381-4763243; i18n-prefs=CNY; ubid-acbcn=459-9924935-4649529; session-token=8Ehx94kxW5kN9ctvDmidHxjUDZn4z1fvEaTEPKyqpfzXQBhGO+SUBn07qnxZCHfgwxXWVydoHNTNUZFokWwxV5wmhcbDmv9epSAfODhe0kHo3PhNIFH+1V949/BzOmtl1CrbOBHQB88D2Ts4det5+rEV+n92ebl5bEAUHHjBr4cK+R05qafLtb3q8vrM0N8p; csm-hit=tb:YDW0RYHKSTEC37GKKT3J+s-YDW0RYHKSTEC37GKKT3J|1649129794386&t:1649129794386&adb:adblk_no; session-id-time=2082787201l'
}

try:
    r = requests.get(url,timeout=30, headers=kv, cookies=cookies)
    r.raise_for_status()
    r.encoding = 'utf-8'
    print(r.text)
except:
    print('失败')