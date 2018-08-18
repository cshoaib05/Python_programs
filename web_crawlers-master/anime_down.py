#! /usr/bin/python

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pynotify
from time import sleep
import os
import re

#Getting search results
anime_list = 'http://animeshow.tv/anime-list.html'
sc = requests.get(anime_list)
soup = BeautifulSoup(sc.text,'lxml')
anime = soup.select('li a')
#print(anime)
search = input('Enter anime name: ')
j = 0
animes = []
for i in range(len(anime)):
    if search in anime[i].text.lower():
        animes.append(anime[i].get('href'))
        print(str(j+1)+'. '+anime[i].text)
        j += 1
        
#Selecting the anime to download
print(animes[0])
user_input = int(input('Enter the anime no. to download: '))
anime_url = animes[user_input-1]

sc = requests.get(anime_url)
soup = BeautifulSoup(sc.text,'lxml')
li = soup.select('#episode-list-entry-tbl a')
print(li)
li.reverse()
epi = re.compile(r'\d+')
print(epi)
mo = epi.search(li[-1].text)
print(mo)
episodes = int(mo.group())
print ('No. of Episodes:'+ episodes)
select = int(input('Enter episode to start: '))

#Downloading episodes
for ep_no in range(select,episodes+1):
    k = ep_no*2
    print ('Downloading Episode'+ep_no)
    pynotify.init('test')
    n = pynotify.Notification('Episode '+str(ep_no)+' released','Firefox Will open Automatically and download will begin shortly')
    n.show()          
    url = 'http://9xbuddy.com/download?url='+li[k-1].get('href')
    driver = webdriver.Firefox()
    driver.get(url)
    sleep (15)
    down = driver.find_element_by_link_text('Download Now')
    href = down.get_attribute('href')
    os.system('wget --output-document '+str(ep.no)+'.mp4 '+href)
    print('\nDownloaded Episode '+str(ep_no))
    driver.quit()

print('All Episodes Downloaded')
