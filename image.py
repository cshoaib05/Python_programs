from bs4 import BeautifulSoup
import requests
from selenium import webdriver


url = r"https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


name_tbody_tag = soup.findAll('td',{'class':'titleColumn'})
rating_td_tag = soup.findAll('td',{'class':'ratingColumn imdbRating'})
link_td_class = soup.findAll('td',{'class':'titleColumn'})

# for each_tag in name_tbody_tag:
# 	print(each_tag.find('a').text)


# for each_tag in rating_td_tag:
# 	print(each_tag.find('strong').text)

name_list = []
rating_list = []
first_link_list = []


for i in range(len(name_tbody_tag)):
	#print(name_tbody_tag[i].find('a').text, "-", rating_td_tag[i].find('strong').text)
	name_list.append(name_tbody_tag[i].find('a').text)
	rating_list.append(rating_td_tag[i].find('strong').text)
	first_link_list.append(link_td_class[i].find('a')['href'])

#print(name_list,rating_list,first_link_list)
third_link_list = []
for each_link in first_link_list:
	each_link = r"http://www.imdb.com"+ each_link
	second_page = requests.get(each_link)
	second_soup = BeautifulSoup(second_page.text,'lxml')
	third_link = second_soup.find('div',{'class':'poster'})
	third_link = third_link.find('a')['href']
	third_link_list.append(third_link)

print(third_link_list)


"""
driver = webdriver.Chrome("D://ArmanK//chromedriver.exe") 

driver.get(url)

img_tag = soup.findAll('img',{'class':'pswp__img'})
link = img_tag[3]['src']

driver.quit()

file = open("1qq.jpg","wb")
file.write(requests.get(link).content)
file.close()
"""