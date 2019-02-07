from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome(executable_path = r"D:\ArmanK\chromedriver.exe")

url = r"https://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv"
# driver.get(url)

# html_doc  = driver.page_source

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'lxml')

#print(soup.prettify())

#lister-list
tbody_tag = soup.find('tbody',{'class':'lister-list'})
TD_name = tbody_tag.findAll('td',{'class':'titleColumn'})
TD_ratings = tbody_tag.findAll('td',{'class':'ratingColumn imdbRating'})


name_list = []
ratins_list = []
final_list = []

for i in range(len(TD_name)):
	name_list.append(TD_name[i].find('a').text)
	ratins_list.append(TD_ratings[i].find('strong').text)
	final_list.append(name_list[i]+" "+ratins_list[i])

#print(final_list)


links = []
for tag in TD_name:
	links.append(tag.find('a')['href'])

#print(links)
third_page_links = []

for each_link in links[:10]:
	second_page = requests.get('https://www.imdb.com'+each_link)
	second_soup = BeautifulSoup(second_page.text,'lxml')
	div_a_tag = second_soup.find('div', {'class':'poster'})

	#print(div_a_tag.find('a')['href'])
	third_page_links.append(div_a_tag.find('a')['href'])

image_links = []
for each_link in third_page_links[:10]:

	url = 'https://www.imdb.com'+each_link
	print(url)
	driver.get(url)
	third_page = driver.page_source

	#third_page = requests.get('https://www.imdb.com'+div_a_tag.find('a')['href'])
	third_soup = BeautifulSoup(third_page,'lxml')
	#print(third_soup)
	img_tag = third_soup.findAll('img',{'class':'pswp__img'})
	#print(img_tag['src'])
	image_links.append(img_tag[3]['src'])

print(image_links)
driver.quit()

for i,each_link in enumerate(image_links):
	f = open('{0}.jpg'.format(name_list[i]),'wb')
	f.write(requests.get(each_link).content)
	f.close()	




#driver.quit()


