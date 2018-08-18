import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib
import requests
from urllib.request import FancyURLopener
import pynotify
from selenium import webdriver

# from scrapy.linkextractors import LinkExtractor

a=[]
word = 'tera yaar hu main'

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
asa = asa.replace('/watch?v=','')
print(asa)

link9x='https://www.flvto.biz/download/direct/mp3/yt_'

DLlink = link9x+asa
print(DLlink)
webbrowser.open(DLlink)
# ytplaylink = yt+matching[0]
#print(ytplaylink)

#webbrowser.open_new_tab(ytplaylink)


'''link9x='https://offmp3.com/process?url='+ytplaylink

# print(link9x)
# webbrowser.open(link9x)
class MyOpener1(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'   # Set this to a string you want for your user agent
	
myopener1 = MyOpener1()
page1 = myopener1.open(link9x).read()
webpage1 = page1.decode('utf-8')

soup1 = bs.BeautifulSoup(webpage1,'lxml')
print(soup1)
div1 = soup1.body
for data1 in div1.find_all(href=True):
	print(data1.get('href'))'''








# <a href="//offmp3.com/process?url=


# aa="https://offmp3.com/process?url=https://youtu.be/EatzcaVJRMs"
# webbrowser.open(aa)

# "http://163.172.46.33/download/c9_pbjcm79R/784b1cdca0cfc204291e42029ffc3f03-1522656494/RnVsbCBWaWRlbzogVGVyYSBZYWFyIEhvb24gTWFpbiB8IFNvbnUgS2UgVGl0dSBLaSBTd2VldHkgfCBBcmlqaXQgU2luZ2ggUm9jaGFrIEtvaGxpIHwgU29uZyAyMDE4"

# https://www.flvto.biz/downloads/mp3/yt_EatzcaVJRMs/

# "EatzcaVJRMs/"

# "http://srv7.youtubemp3.to/download.php?output=MjQ2Mzk3NDQvMTUyMjY0NTAzMw=="