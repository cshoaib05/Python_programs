from __future__ import absolute_import
import json
import socket
from word2number import w2n
import urllib
import pyowm
import bs4 as bs
from urllib.request import FancyURLopener
import clipboard
import imdb
from tkinter import *

from tkinter import messagebox
import youtube_dl

try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request

import apiai

from gtts import gTTS
import speech_recognition as sr
import os, random
import subprocess
from bs4 import BeautifulSoup
from win32com.client import Dispatch
import re
import sys
import webbrowser
import smtplib
import pyttsx3
import requests
import playsound
import time
import wikipedia
import wolframalpha
import datetime
import gsearch
# from weather import Weather


CLIENT_ACCESS_TOKEN = os.environ.get('API_AI_TOKEN', '3b0e24b4a9754d8b977392a250774aaf')
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

request = ai.text_request()

request.session_id = os.environ.get(
    'API_AI_SESSION_ID', 'dd60fde7-c6ab-4f38-9487-7300c42b4916')



#Taskkill /IM chrome.exe /F

def typeCommand():
    inp = input("ME :")
    print("")
    return inp 

def gsearch(word):
    url="http://www.google.com/?#q="
    webbrowser.open_new_tab(url+word)

def ysearch(word):
    url="http://www.youtube.com/results?search_query="
    webbrowser.open_new_tab(url+word)




def talkToMe(audio):
    "speaks audio passed as argument"
    #os.system('nircmd.exe killprocess wmplayer.exe')
    #speak = Dispatch("SAPI.SpVoice")
    #speak.Rate(5)
    #speak.Speak(audio)
    #print(audio)
    #myCommand()




    '''def onWord(name,location ,length):

            #location=0
        print('location',location)s
        if(location<len(audio) and location>20 and engine.isBusy()):
            stopCommand()
            engine.say("ok")
            return'''

        #audio="a"

    #if('stop' in audio):
     #   engine.stop()
      #  #start()
       # engine.endloop()
       # engine.disconnect()
       # assistant(myCommand())

   
    #engine.connect('started-word', onWord)
    print("Asistnt: "+audio)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+0)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    engine.say(audio)
    #engine.connect('started-word', onWord)
    
    engine.runAndWait()
   #assistant(myCommand())        
    #return                
        
        

    #voices = eng.getProperty('voices')
    #eng.setProperty('voice', voices[2].id)
    #eng.say(audio)
    #eng.runAndWait()
    #def onWord(name, location, length):
       # print ('word', name, location, length)
       #if (engine.isBusy()):
        #location=myCommand()
        #if(location=='stop'):
            #engine.stop()

    
    
    
    #onWord()
    '''for line in audio.splitlines():
        #  use the system's inbuilt say command instead of mpg123
        text_to_speech = gTTS(text=audio, lang='en-us', slow=False)
        print(text_to_speech.save('audio.mp3'))
        
        print(str(text_to_speech))
        
        #playsound.playsound('audio.mp3', True)
        #playsound.playsound('audio.mp3', False)
        #os.system('mpg123 audio.mp3')
        #assistant(interCommand())
        #assistant(myCommand())
        #os.system('start "" "D:\\ArmanK\\python programs\\SUBLIME FILES\\SpeechRecog\\audio.mp3"')
        #assistant(myCommand())
        
        '''

'''def stopCommand():
    r = sr.Recognizer()

    +
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        print('Ready...Stop')
        r.adjust_for_ambient_noise(source, duration=1)
        stopaudio = r.listen(source,phrase_time_limit=10)
        stopcommand = r.recognize_google(stopaudio).lower()
        print('You Said: ' + stopcommand + '\n')
        if('stop' in stopcommand):
                print("In iff stopcommand")
                engine.stop()
        #start()
                engine.endloop()
                engine.disconnect()
                sys.exit()
        #talkToMe('Tumne ye bola: ' + command)
    return  
'''

    #loop back to continue to listen for commands if unrecognizable speech is received
   # except sr.UnknownValueError:
        #print('Your last command couldn\'t be heard')
        #talkToMe("missed your words")
    #    print("missed your words in stopcommand")
        #stopcommand = stopCommand();
     #   return
        
    #except:
    #    print("No Internet connection bye")
    #    talkToMe("No Internet connection bye")
     #   sys.exit()

    #talkToMe(stopcommand)
    #return stopcommand
    #return

    

def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        #r.pause_threshold = 1
        print('Ready...')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,phrase_time_limit=10)

    try:
        command = r.recognize_google(audio).lower()
        #talkToMe('Tumne ye bola: ' + command)
        print('You Said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        #print('Your last command couldn\'t be heard')
        #talkToMe("missed your words")
        print("missed your words")
        command = myCommand();
    except:
        print("No Internet connection bye")
        talkToMe("No Internet connection bye")
        sys.exit()

    
    return command




def assistant(command):
    "if statements for executing commands"
    #os.system('nircmd.exe killprocess wmplayer.exe')


        

    if command == "hello1" or command == "hi1" or command=="hey1":
        print("hello ")
        talkToMe("hello sir")

    elif command == "what time is it" or command == "tell me time" or command == "what's the time" or command == "time" or command == "what is today" or command == "what's today" :
        t = time.asctime(time.localtime(time.time()))
        talkToMe(t)


    elif command == "bye" or command == "buy" or command=='exit':
        if hr >= 20 and hr <=24:
            print("Good night\n")
            talkToMe("Good night")
            sys.exit()
        else:
            print("see you again \n")
            talkToMe("see you again ")
            sys.exit()

    elif command == "how are you1":
        print("I'm good. How are you?\n")
        talkToMe("I'm good. How are you?")

    elif command == "ok1" or command == 'okay1' or command == 'yeah1':
        print("Yes")
        talkToMe("yes")
    

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'movie' in command:
        command =  command.replace("about movie","")
        command = command.title()

        print("Name of a movie:"+command.replace("about movie",""))
        #try:
        app = imdb.IMDb()
        results = app.search_movie(command)
        #if not results:
        #breturn "error 404"
        first = results[0]
        ID = first.movieID
        data = app.get_movie(ID)
        talkToMe("Year: "+str(data['year']))
        talkToMe("IMDb ratings: "+str(data['rating']))
        #except:
         #   talkToMe("Error 404")


    elif 'google' in command or 'images of' in command or 'image of' in command or 'google map' in command:
        
        if 'images' in command:
            url = "https://www.google.com/search?tbm=isch&q={}".format(command.replace("images of", ""))
            webbrowser.open(url)

        
        #command=command.replace('on',"")
        elif 'google map' in command:
            url = "https://www.google.co.in/maps/place/" + command.replace("google map","")
            webbrowser.open(url)

        else:
            command=command.replace('google',"")
            gsearch(command)






    elif 'youtube' in command or "video" in command:

        command=command.replace("on","")
        command=command.replace("search","")

        if 'play' in command:
            command=command.replace("play","")
            command=command.replace("on","")
            command=command.replace("youtube","")
            try:
                def ytDownloader(word):
                    a=[]
                    #word = input()

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
                # print(matching[0])

                    ytplaylink = yt+matching[0]

                # print(ytplaylink)
                # pwrshllink= 'powershell -command Invoke-WebRequest '+ytplaylink+' -OutFile '+word+'.mp3'
                    webbrowser.open_new_tab(ytplaylink)

                ytDownloader(command)
            except:
                ytDownloader(command)

        if "download" in command:
            command=command.replace("video","")
            command=command.replace("download","")
            a1=[]
            a11=[]
            word1 =command #input('ENTER THE VIDEO NAME TO DOWNLOAD')

            url1 = 'https://www.youtube.com/results?search_query=+'+word1
            yt1='https://www.youtube.com'
            #webbrowser.open_new_tab(url)

            class MyOpener1(FancyURLopener):
                version1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'   # Set this to a string you want for your user agent
            myopener1 = MyOpener1()
            page1 = myopener1.open(url1).read()
            webpage1 = page1.decode('utf-8')

            soup1 = bs.BeautifulSoup(webpage1,'lxml')

            div1 = soup1.body
            for data1 in div1.find_all(href=True):
                a1.append(data1.get('href'))

            #print(a)

            matching1 = [s1 for s1 in a1 if '/watch?' in s1]

            ytplaylink1 = yt1+matching1[0]

            print(ytplaylink1)
            #os.walk(r"D:\ArmanK\python programs\SUBLIME FILES\SpeechRecog\video")
            os.system('"cd E:\\VIDEOS" & youtube-dl -f 22 '+ytplaylink1)

        else:
            ysearch(command.replace('youtube',""))

    elif 'joke' in command:
        res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('hahaha')

    elif 'facts' in command:
        fw = open('.facts.txt',encoding="utf8")
        facts = fw.read()
        facts = facts.split('\n')
        while True:    
            i = random.randrange(0,len(facts)-1)
            #print(facts[i])
            talkToMe(facts[i])
            break

    elif 'quotes' in command:
        fw = open('.quotes.txt','r')
        vocab = fw.read()
        vocab = vocab.split('\n')

        while True:
            i = random.randint(0,2002)
            if i % 2 == 0:
                if len(vocab[i]) < 118:
                    #sendmessage(vocab[i],vocab[i+1])
                    #print(vocab[i]+" said by "+vocab[i+1])
                    talkToMe(vocab[i]+" said by "+vocab[i+1])
                    break
                else:
                    continue
            else:
                continue

    elif 'teach me some word' in command:
        fw = open('.vocab.txt','r')
        vocab = fw.read()
        vocab = vocab.split('\n')

        while True:
            i = random.randint(0,len(vocab)-1)
            if i % 2 == 0:
                #sendmessage(vocab[i],vocab[i+1])
                print(vocab[i]+"--"+vocab[i+1])
                for j in range(3):
                    talkToMe(vocab[i]+". meaning ."+vocab[i+1]+".")
                break
            else:
                continue

    elif 'cricket score' in command:
        url = "http://static.cricinfo.com/rss/livescores.xml"
        sc = requests.get(url)
        soup = BeautifulSoup(sc.text,'lxml')

        i = 1
        for data in soup.findAll('item'):
            print(str(i)+'. '+data.find('description').text)
            i += 1
         

        '''for i in range(10):
            url = 'http://www.snapple.com/real-facts/list-view/'+str(i+1)
            print('url:',url)       
            sc = requests.get(url)
            soup = BeautifulSoup(sc.text,'lxml')
            fact = soup.findAll('p',{'class':'fact_detail'})
            print('fact:',fact)
            for i in range(len(fact)):
                fw.write(fact[i].text+'\n')
        '''

    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'armaan' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('Arman Khan', 'ak682015@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')


    elif 'lock'== command:
        subprocess.call('rundll32.exe user32.dll,LockWorkStation')

    elif 'new folder' in command:
        os.system('mkdir ad')

    elif 'new file' in command:
        talkToMe("name of a file?")
        #name=str(myCommand())
        name=str(typeCommand())
        if('python' in command):
            os.system('NUL >'+ name+'.py')
        else:
            os.system('NUL >'+name+'.txt')
        talkToMe("File Created")

    elif 'open chrome' in command:
        os.system('start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
    elif 'close chrome' in command:
        os.system('nircmd.exe killprocess chrome.exe')
    elif 'vlc' in command:
        os.system('start "" "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"')
    elif 'sublime' in command:
        os.system('start "" "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text 3.lnk"') 
    elif 'cmd' in command:
        os.system('start "" "C:\WINDOWS\system32\cmd.exe"')

    elif 'take a note' in command:


        f = open('Notes.txt','a')
        t = time.asctime(time.localtime(time.time()))
        f.write('\n'+t+'\n'+command.replace('take a note that',"")) 
        f.close()
        talkToMe("Done")

    elif 'read my notes' in command:
        f = open('Notes.txt','r')
        talkToMe(f.read())
        f.close()

    elif 'clear my notes' in command:
        f = open('Notes.txt','w')
        f.close()
        talkToMe("Done")

    elif 'open my notes' in command:
        os.system('start "" "D:\\PYTHON"')

    elif 'minimise all' in command:
        os.system('nircmd sendkeypress rwin+"d"')

    elif 'maximise all' in command:
        os.system('nircmd sendkeypress rwin+shift+"m"')

    elif 'max volume' in command or 'full volume' in command or 'volume max' in command or 'volume' in command:
        os.system('nircmd.exe mutesysvolume 0')

    elif 'increase volume' in command or 'volume up' in command:
        os.system('nircmd.exe changesysvolume 10000')

    elif 'decrease volume' in command or 'volume down' in command:
        os.system('nircmd.exe changesysvolume -10000')

    elif 'silent' in command:
        os.system('nircmd.exe mutesysvolume 1')

    elif 'low brightness' in command or 'low light' in command:
        os.system('nircmd.exe setbrightness 5')
    elif 'medium brightness' in command or 'medium light' in command:
        os.system('nircmd.exe setbrightness 50')
    elif 'full brightness' in command or 'max light' in command: 
        os.system('nircmd.exe setbrightness 100')
    elif 'screen of' in command:
        os.system('nircmd.exe monitor off')
    elif 'screen on' in command:
        os.system('nircmd sendkeypress ctrl')
    elif 'empty bin' in command:
        os.system('nircmd.exe emptybin')

    elif 'play some music' in command or 'play music' in command:
        a=str(random.choice(os.listdir("E:\\MUSIC")))
        path = "E:\\MUSIC"+'\\'+a
        os.system('"'+path+'"')

    elif 'play song' in command:

        command=command.title()
        for root, dirs,files in os.walk("E:\\MUSIC"):
            for file in files:
                if command.replace('Play Song',"") in file.replace('_',' '):
                    path = "E:\\MUSIC"+'\\'+file            
                    os.system(path)
                    break
            else:
                talkToMe("Song Not Found Please Download it")

        #if 'video' in command:
         #   command=command.title()





    elif 'next' in command:
        a=str(random.choice(os.listdir("E:\\MUSIC")))
        path = "E:\\MUSIC"+'\\'+a
        os.system(path)

    elif 'stop music'in command:
        os.system('nircmd.exe killprocess wmplayer.exe')

    elif 'task manager' in command:
        os.system('nircmd sendkeypress ctrl+shift+esc')

    elif 'clipboard' in command or 'clip board' in command:
        talkToMe(clipboard.paste())

    elif 'calculate' in command:

        value = command.replace("what's ", "")
        value = command.replace("calculate","")
        value = value.replace(" times", "*")
        value = value.replace(" plus", "+")
        value = value.replace(" minus", "-")
        value = value.replace(" divides", "/")
        value = value.replace(" divide", "/")
        value = value.replace(" x", "*")
        print(value)

        try:
            
            finalValue = eval(value)
            #print(finalValue)
            #eval(finalValue)
            talkToMe(finalValue)
                

        except:
            try:
                client = wolframalpha.Client("4E3H79-A3ARKHYKU9")
                #print('command:',command)
                res = client.query(command)
                answer = next(res.results).text
                #print(answer)

                #print("IN WIKI")
                talkToMe(answer)
            except:
                talkToMe("I don't Understand")

    elif 'current temperature' in command:
        owm = pyowm.OWM('3b8dc8474c4fdddfea2631f41f134a97')  
        obs = owm.weather_at_place("Mumbai,in")  
        temperature=obs.get_weather().get_temperature('celsius')
        talkToMe("The temperature is "+str(temperature['temp_max'])+" degree celsius")

    elif 'change wallpaper' in command:
        a=str(random.choice(os.listdir("D:\\ArmanK\\python programs\\SUBLIME FILES\\SpeechRecog\\images")))
        print('a',a)
        pic_path = "D:\\ArmanK\\python programs\\SUBLIME FILES\\SpeechRecog\\images"+'\\'+a
        print('pic_path',pic_path)
        cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' %pic_path
        os.system(cmd)
        os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
        os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
        print('Wallpaper is set.')


    elif 'open' in command:
        #command = 'open notepad'
        command = command.replace('open',"")
        command = command.replace(" ","")
        
        os.system('nircmd sendkeypress rwin')
        for i in command:
            os.system('nircmd sendkeypress '+i)
        os.system('nircmd sendkeypress enter')

    elif 'news' in command:
        req = Request('https://www.google.com/search?q=news&client=firefox-b-ab&source=lnms&tbm=nws&sa=X&ved=0ahUKEwiwo5iM-pHaAhUIqo8KHSlQBbwQ_AUIDCgD&biw=1366&bih=654', headers={'User-Agent': 'Mozilla/5.0'})

        web_byte = urlopen(req).read()
        webpage = web_byte.decode('utf-8')

        soup = bs.BeautifulSoup(webpage,'lxml')

        div = soup.body

        for data in div.find_all('h3'):
            news=data.text
            print(news)








    elif ('do' in command or 'thank' in command or 'yeah' in command or 'yes' in command or 'okay' in command or 'ok' in command or 'great' in command or 'nice' in command or 'awesome' in command or 'excellent' in command or 'hi' in command or 'hey' in command or 'good' in command or 'lol' in command or 'haha' in command or 'hello' in command or 'what' in command or 'where' in command or 'who' in command or 'whose' in command or 'when' in command or 'how' in command or 'whom' in command or 'why' in command or 'which' in command):
        #talkToMe('I don\'t know what you mean!')
        try:
            request = ai.text_request()
            request.query = command
            response = request.getresponse().read()
            output = json.loads(response)
            answer = output["result"]["fulfillment"]["speech"]
            #print('answer:',answer)
            #talkToMe(answer)

            if(answer=="" or answer=="not found"):
                #talkToMe(answer+" on layer 1")
                try:
                    
                    client = wolframalpha.Client("4E3H79-A3ARKHYKU9")
                    #print('command:',command)
                    res = client.query(command)
                    answer = next(res.results).text
                    #print(answer)
                    talkToMe(answer)
                    #talkToMe("improve your internet speed")
                except:
                    try:
                        
                        print("IN WIKI")
                        talkToMe(wikipedia.summary(command))
                        #talkToMe("improve your internet speed")
                    except:
                        talkToMe("I can't Understand what you said")
            else:
                talkToMe(answer)
                pass
        except:
            pass

    elif (command==""):
        assistant(typeCommand())
            


            

    else:
        request = ai.text_request()
        request.query = command
        response = request.getresponse().read()
        output = json.loads(response)
        answer = output["result"]["fulfillment"]["speech"]
        #talkToMe(answer)
        if(answer=="" or answer=="not found"):

            talkToMe("What "+command+"? "+"do you want me to search deeply?")
            #if(myCommand()=='yes'):
            if(typeCommand()=="yes"):
                try:
                    client = wolframalpha.Client("4E3H79-A3ARKHYKU9")
                    #print('command:',command)
                    res = client.query(command)
                    answer = next(res.results).text
                    #print(answer)

                    #print("IN WIKI")
                    talkToMe(answer)
                    #talkToMe("improve your internet speed")

                except:

                    try:
                        #print(wikipedia.summary(command))
                        
                        print("IN WIKI")
                        talkToMe(wikipedia.summary(command))
                        #talkToMe("improve your internet speed")
                    except:
                        talkToMe("Even internet has no answer about it.")
            else:
                talkToMe("OK, ask me some thing else")

        else:
            talkToMe(answer)


now = datetime.datetime.now()
hr=now.hour
#print(hr)

if (hr < 12):
    #print("Good moring. Have a nice day")
    talkToMe("Good moring. Have a nice day!")
elif (hr >= 12 and hr < 17):
    #print("Good afternoon")
    talkToMe("Good afternoon!")
elif (hr >= 17 and hr <= 24):
    #print("Good Evening")
    talkToMe("Good Evening!")

#talkToMe('Hello')

#loop to continue executing multiple commands
def start():
    while True:
        #assistant(myCommand())
        assistant(typeCommand())#
start()