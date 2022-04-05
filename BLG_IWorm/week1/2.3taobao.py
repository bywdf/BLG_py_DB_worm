import requests

url = 'https://detail.tmall.com/item.htm?id=563729455746&spm=a1z02.1.2016030118.d2016038.0ZmvJP&scm=1007.10157.81291.100200300000000&pvid=7d1b8b18-33ad-4f46-9725-8e47305b71cb&skuId=4576486769183'
kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'}
cookies = {
    'Cookie':'enc=x8r8/FXdZS/Vn6tHGg+/fvb66UojV1GRVSzCeO57I1/82lCaeNFXWGzNhKDiRYp/lGIklBDRendYN14rlnGHrw==; t=827e79448c2e51e549a59014e5679ef2; _tb_token_=ea776f17778a8; cookie2=1284a07b04b90179f7871a932218a8b3; pnm_cku822=098#E1hvx9vUvbpvUvCkvvvvvjiWR2chsjDWnLdy6j1VPmPUzj18RLSW6jYVPFSh6jDvi9hvCvvv9UUvvpvVvvpvvhCvmvhvLvCXBvvjpdVxrXZzRFn1txVH5oJQbZk9k87tRbI6HuoQD704d5ln+Exr68TJwHAxfa3l53h5prhH6ahtrmEc6X7U+b8raoF6QbmD5iAUvpvVmvvC9jDvuvhvmvvv9b/zpfDLKvhv8vvvvvCvpvvvvvm2phCv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvRvpvhvv2MMs9Cvvpvvvvv; cna=lrI7GBMaKxUCAd0CYCqyO2Q4; xlly_s=1; tfstk=c-vdBdwbYV0hmPI90BhMPkZv73JdZT0R5k_uecm3QnYg4TeRi_JDHxGZOg_VJcC..; l=eBSaUCRuQBUZvZIzXOfZnurza77TIIRAguPzaNbMiOCPOMfp5JLAW6VGtaY9CnGVh6xeR3yxiRLwBeYBqCb-OJ7Fa6Fy_IHmn; isg=BLe3XRFYmcWRuiGDW0i30AgbRqsBfIveSAM4iwlk2QbtuNf6EU_DL0fanhjmUGNW; dnk=wdf1226; uc1=cookie21=V32FPkk/hoKjSfNGfL3AxQ==&pas=0&cookie15=VT5L2FSpMGV7TQ==&existShop=true&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw==&cookie14=UoewCZVjYK8qzQ==; uc3=vt3=F8dCvCtLpOjx9csFdkg=&nk2=FP0fBgPKQg==&lg2=WqG3DMC9VAQiUQ==&id2=WvKQyoqJgtc=; tracknick=wdf1226; lid=wdf1226; uc4=nk4=0@Fnb+6lGelZZBnICaUk+EOSHu&id4=0@WDWjM0p5A5d8l3Qd9zqPdEd21g==; _l_g_=Ug==; unb=92798200; lgc=wdf1226; cookie1=AiUAV0463AsbDGAVqP1yAaa7CFv9eYba9wL7/X4fTnc=; login=true; cookie17=WvKQyoqJgtc=; _nk_=wdf1226; sgcookie=E100AQRMVag6X7F/jiU3SPf2qjZHbnnvw/NWiFKnweAxcud3pVRU8O1jGiRq/SMRXITehLPQ+kl25xhsvZlLITO7bNInwYT8k9q4mgGA3xWN7rXmSVIbSXQqhouF6OdbxcZz; cancelledSubSites=empty; sg=609; csg=75ae2310'
}

try:
    r = requests.get(url,timeout=30, headers=kv, cookies=cookies)
    r.raise_for_status()
    r.encoding = 'utf-8'
    print(r.text[:2000])
except:
    print('失败')