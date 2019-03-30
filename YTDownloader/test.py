import webbrowser
import bs4 as bs
from urllib.request import Request, urlopen
import urllib
import requests
from urllib.request import FancyURLopener
import pynotify
from selenium import webdriver
import youtube_dl
import os
# import ffprobe


a=[]
a1=[]
word = 'Science of Swing Bowling | Hindi'#input('ENTER THE VIDEO NAME TO DOWNLOAD')

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

ytplaylink = yt+matching[0]

print(ytplaylink)
# def download():
r=os.system('youtube-dl -f 136 https://9anime.ru/watch/amnesia-dub.v7kv/84o3rq')
			# download()

# download()
#webbrowser.open_new_tab(ytplaylink)