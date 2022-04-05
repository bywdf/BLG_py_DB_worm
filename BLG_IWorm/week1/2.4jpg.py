import requests
import os

url = 'https://ngimages.oss-cn-beijing.aliyuncs.com/2022/03/25/2e4280c9-f14f-434d-9161-e60f151388fa.jpg'
kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'}
cookies = {
    'Cookie':'Hm_lvt_ca8fdc4afd8dbaec0d0f29ebf69ff42a=1649134577; Hm_lpvt_ca8fdc4afd8dbaec0d0f29ebf69ff42a=1649134577'
}
root = 'D://pics//'
npath = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(npath):
        r = requests.get(url, headers=kv)
        with open(npath, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功!')
    else:
        print('文件已经存在')
except:
    print('文件爬取失败')