import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib 
import requests
from urllib.request import FancyURLopener
a=[]
word='shahrukh khan'
url = 'https://www.news18.com/newstopics/'+word
# webbrowser.open(url)

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'    #Set this to a string you want for your user agent

myopener = MyOpener()
page = myopener.open(url).read()
webpage = page.decode('utf-8')

soup = bs.BeautifulSoup(webpage,'lxml')
div = soup.body
for data in div.find_all('p'):
	a.append(data.text)
print(a[0],a[1],a[2])
