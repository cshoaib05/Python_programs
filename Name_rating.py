from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# driver = webdriver.Chrome(executable_path = r"D:\ArmanK\chromedriver.exe")

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

print(final_list)

#driver.quit()


