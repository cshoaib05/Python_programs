from gtts import gTTS
import speech_recognition as sr
import os, random
import subprocess
import re
import sys
import webbrowser
import smtplib
import requests
import playsound
import time
import wikipedia
import wolframalpha



def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    # engine = pyttsx.init()
    # engine.say(audio)
    # engine.runAndWait()
    for line in audio.splitlines():
        #  use the system's inbuilt say command instead of mpg123
        text_to_speech = gTTS(text=audio, lang='hi', slow=False)
        text_to_speech.save('audio.mp3')
        #playsound.playsound('audio.mp3', True)
        os.system("mpg123 audio.mp3")

def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        #talkToMe('Tumne ye bola: ' + command)
        print('You Said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        #print('Your last command couldn\'t be heard')
        talkToMe("missed your words")
        command = myCommand();

    return command

def typeCommnad():
    command = input("E:")
    print('You Said: ' + command + '\n')
    return command



def assistant(command):
    "if statements for executing commands"

    if 'time' in command:
        t = time.asctime(time.localtime(time.time()))
        talkToMe(t) 
        #print(t)
    

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'joke' in command:
        res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('hahaha')

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


    elif 'lock' in command:
        subprocess.call('rundll32.exe user32.dll,LockWorkStation')

    elif 'new folder' in command:
        os.system('mkdir ad')

    elif 'new file' in command:
        talkToMe("name of a file?")
        name=str(myCommand())
        if('python' in command):
            os.system('NUL >'+ name+'.py')
        else:
            os.system('NUL >'+name+'.txt')
        talkToMe("File Created")

    elif 'bye' in command:
        talkToMe("Ok Bye See Yaa")
        #print("Ok Bye See Yaa")
        sys.exit()

    elif 'open google chrome' in command:
        os.system('start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
    elif 'vlc' in command:
        os.system('start "" "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"')
    elif 'sublime' in command:
        os.system('start "" "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text 3.lnk"') 

    elif 'take a note' in command:
        f = open('Notes.txt','a')
        t = time.asctime(time.localtime(time.time()))
        f.write('\n'+t+'\n'+command.strip('take a note that')) 
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
        os.system('start "" "D:\\ArmanK\\python programs\\SUBLIME FILES\\SpeechRecog\\Notes.txt"')

    elif 'minimise all' in command:
        os.system('nircmd sendkeypress capslock')

    elif 'volume' in command:
        os.system('nircmd.exe mutesysvolume 0')

    elif 'silent' in command:
        os.system('nircmd.exe mutesysvolume 1')

    elif 'reduce light' in command:
        os.system('nircmd.exe setbrightness 30')

    elif 'medium light' in command:
        os.system('nircmd.exe setbrightness 50')

    elif 'more light' in command:
        os.system('nircmd.exe setbrightness 80')
    
    elif 'light of' in command:
        os.system('nircmd.exe monitor off')

    elif 'empty' in command:
        os.system('nircmd.exe emptybin')

    elif 'play music' in command:
        a=str(random.choice(os.listdir("E:\MUSIC")))
        path = "E:\MUSIC"+'\\'+a
        os.system(path)

    elif 'change' in command:
        a=str(random.choice(os.listdir("E:\MUSIC")))
        path = "E:\MUSIC"+'\\'+a
        os.system(path)

    elif 'stop music' in command:
        os.system('nircmd.exe killprocess RuntimeBroker.exe')

    elif 'task manager' in command:
        os.system('nircmd sendkeypress ctrl+shift+esc')



    else:
        #talkToMe('I don\'t know what you mean!')
        try:

            client = wolframalpha.Client("6R7AEW-Y2GV77UAPP")
            #print('command:',command)
            res = client.query(command)
            answer = next(res.results).text
            print(answer)
            #talkToMe(answer)

        except:

            try:
                print(wikipedia.summary(command))
            except:
                #talkToMe("I can't Understand what you said")
                print("I can't Understand what you said")



talkToMe('Hello')
#print('Hello')
#loop to continue executing multiple commands
while True:
    assistant(myCommand())