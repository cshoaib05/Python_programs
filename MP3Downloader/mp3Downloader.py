import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib
import requests
from urllib.request import FancyURLopener
import os

# from scrapy.linkextractors import LinkExtractor
# path = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
# driver=webdriver.Firefox(path)
a=[]
word = input('ENTER THE SONG NAME:')

url = 'https://www.youtube.com/results?search_query=+'+word
yt='https://www.youtube.com'
#webbrowser.open_new_tab(url)
class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'   # Set this to a string you want for your user agent

myopener = MyOpener()
page = myopener.open(url).read()
webpage = page.decode('utf-8')

soup = bs.BeautifulSoup(webpage,'lxml')

div = soup.body
for data in div.find_all(href=True):
	a.append(data.get('href'))

	#print(a)

matching = [s for s in a if '/watch?' in s]
asa =matching[0]
print(asa)
asa = asa.replace('/watch?v=','')
print(asa)
# webbrowser.open(DLlink)

ytplaylink = yt+matching[0]
print(ytplaylink)
word = word.replace(" ","_")
word = '1_'+word
os.system('"cd E:\\MUSIC" && youtube-dl --output '+word+'.%(ext)s -i --extract-audio --audio-format mp3 --audio-quality 0 '+ytplaylink)

#webbrowser.open_new_tab(ytplaylink)
 