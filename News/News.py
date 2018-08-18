import bs4 as bs
from urllib.request import Request, urlopen

req = Request('https://www.google.com/search?q=news&client=firefox-b-ab&source=lnms&tbm=nws&sa=X&ved=0ahUKEwiwo5iM-pHaAhUIqo8KHSlQBbwQ_AUIDCgD&biw=1366&bih=654', headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')

soup = bs.BeautifulSoup(webpage,'lxml')

div = soup.body

for data in div.find_all('h3'):
	news=data.text
	print(news)