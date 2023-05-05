from bs4 import BeautifulSoup
import requests

url = 'http://python123.io/ws/demo.html'

try:
    r = requests.get(url)
    r.raise_for_status()
    demo = r.text
except:
    pass

soup = BeautifulSoup(demo, 'html.parser')

a = soup.find_all(class_="course")

print(a)