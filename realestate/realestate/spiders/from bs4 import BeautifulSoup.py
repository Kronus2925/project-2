from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.domiporta.pl/mieszkanie/sprzedam?PageNumber=17'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content,'lxml')

x=  soup.find('meta', itemprop="addressRegion")['content']
print(x)




