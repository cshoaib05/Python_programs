#! /usr/bin/python
import requests
from bs4 import BeautifulSoup
import pynotify
import pyperclip
from time import sleep
import os

os.system('echo -n | xclip -selection clipboard')
while True:
    movie = pyperclip.paste()
    if movie != '':
        fw = open('search.txt','a')
        fw.write(movie+'\n')
        fw.close()
        url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie+'&s=all'
        pyperclip.copy('')
        print 'You searched for '+movie
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')

        for td in soup.findAll('td',{'class':'result_text'}):
            href = td.find('a')['href']
            movie_page = 'http://www.imdb.com'+href
            break

        def get_title(movie_url):
            source_code = requests.get(movie_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            for title in soup.findAll('div',{'class':'title_wrapper'}):
                return title.find('h1').text.rstrip()

        movie_name = get_title(movie_page)

        def get_movie_data(movie_url):
            source_code = requests.get(movie_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            div = soup.findAll('div',{'class':'ratingValue'})
            div2 = soup.findAll('div',{'class':'summary_text'})
            genre = soup.findAll('div',{'class':'see-more inline canwrap'})
            if genre[0].find('h4').text == 'Genres:':
                genre = genre[0].find_all('a')
            else:
                genre = genre[1].find_all('a')
            for i in range(len(genre)):
                genre[i] = genre[i].text
            genre = (' | ').join(genre)
            print genre
            pynotify.init('test')
            n = pynotify.Notification(movie_name+' '+div[0].text,genre+'\n'+div2[0].text.lstrip())
            n.show()

        get_movie_data(movie_page)
    print 'copy a movie name to search'
    sleep(5)

'''print_genre = soup.findAll('div',{'class':'subtext'})
for div in print_genre:
    for genre in print_genre.findAll('a'):
        print (genre.text,end=' |')
        print ()'''

