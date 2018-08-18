import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib 
import requests
from urllib.request import FancyURLopener
import json

word='translate goat in hindi'
url = 'https://www.google.co.in/search?hl=en&source=hp&ei=a7bHWtq7KMSCvQS4jpQg&q=transalate&oq=transalate&gs_l=psy-ab.3..0i10k1l10.1870.4240.0.4456.11.10.0.0.0.0.156.946.0j8.8.0....0...1c.1.64.psy-ab..3.8.940.0..0j35i39k1j0i131k1j0i20i263k1j0i67k1j0i131i67k1.0.SowIEnN5d2Q'
# webbrowser.open(url)

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'    #Set this to a string you want for your user agent

myopener = MyOpener()
page = myopener.open(url).read()
webpage = page.decode('utf-8')

soup = bs.BeautifulSoup(webpage).read()

data = json.loads(soup.find('script'))
print(data)
# div = soup.body
# for data in div.find_all('a'):
# 	print(data.text)


