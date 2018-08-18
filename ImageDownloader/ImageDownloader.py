import subprocess
import bs4 as bs
from urllib.request import Request, urlopen
import webbrowser
from urllib.request import FancyURLopener
from selenium import webdriver
import os
import subprocess
import sys


a=[]
#url = 'https://www.google.co.in/search?q=cat&source=lnms&tbm=isch&sa=X&ved=0ahUKEwikvp7D6ZjaAhVKvY8KHQxxBuMQ_AUICigB&biw=1366&bih=654'
word = 'srk'
#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./SamplePowershell\";", "&addOne(10)"])
url='https://www.google.com/search?tbm=isch&q='+word
#webbrowser.open(url)
class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'   # Set this to a string you want for your user agent
	
myopener = MyOpener()
page = myopener.open(url).read()
webpage = page.decode('utf-8')

soup = bs.BeautifulSoup(webpage,'lxml')

div = soup.body
for data in div.find_all('img'):
	link=data.get('src')
	print(link)

pwrshllink= 'powershell -command Invoke-WebRequest '+link+' -OutFile '+word+'.jpg'
#webbrowser.open(link)

# os.system('powershell.exe '+pwrshllink)

# p = subprocess.Popen(['powershell.exe', pwrshllink], stdout=sys.stdout)

# urlretrieve(url.replace('_1366x768', '_1920x1200')