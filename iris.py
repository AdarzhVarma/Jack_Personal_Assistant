from ntpath import join
from pickle import APPEND
from urllib.request import urlopen
import newsapi
import pyttsx3 
import datetime
from pywhatkit.help import exceptions
import speech_recognition as sr
import smtplib
from secrets import senderemail,epwd,to
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import clipboard
import requests
import os 
import pyjokes
import time as tt 
import string
import random
import psutil
import subprocess
import json
from nltk.tokenize import word_tokenize
from newsapi import NewsApiClient
import ctypes






engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices=engine.getProperty('voices')
    #print(voices[1].id)
    if voice==1:
        engine.setProperty('voice',voices[0].id)
        speak("Welcome back !")
        speak("jack at your service, please tell me how can i help you?")

    if voice==2:
        engine.setProperty('voice',voices[1].id)
        speak("Welcome back !")
        speak("iris at your service, please tell me how can i help you?")
        
    

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is:")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good morning !")
    elif hour >= 12 and hour <18:
        speak(" Good afternoon !")
    elif hour >= 18 and hour <24:
        speak(" Good evening sir!")
    else:
        speak(" Good Night sir!")
def wishme():
    greeting()
    speak("Welcome back !")
    speak("jack at your service, please tell me how can i help you?")

#wishme()


# while True:
#     voice=int(input("press 1 for male assistant\npress 2 for female assistant\n"))
#     speak(audio)

    #getvoices(voice)




def takeCommandCMD():
    query=input("Please Tell Me how can i help you?\n")
    return query

def takeCommandMic():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)    

    try:
        print("Recognizing.....") 
        query = r.recognize_google(audio , language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Pardon Please")
        return "None"
    return query  

def sendEmail(content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)
    server.sendmail(senderemail,to, content)
    server.close()

def searchgoogle():
    speak("what should i serach for?")
    search=takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)
    

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')





def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

# def covid():
#     r = requests.get('https://coronavirus-19-api.herokuapp.com/all') 

#     data = r.json()
#     covid_data = f'Confirmed Cases :{data["Cases"]} \n Deaths :{data["deaths"]}  \n Recovered {data["Recovered"]}'
#     print(covid_data)
#     speak(covid_data)

def screenshot():
    name_img= tt.tt()
    name_img = f'A:\\jarvis\\Screenshots\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation


    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2)) 
    s.extend(list(s3)) 
    s.extend(list(s4))  

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    
if __name__=="__main__":
    getvoices(1)
    wakeword= "jack"
    while True:
        query = takeCommandMic().lower()
        query=word_tokenize(query)
        #print(query)
        if wakeword in query:
        
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'wish' in query:
                greeting() 
            elif 'email' in query:
                try:
                    speak('what should i say')
                    content=takeCommandMic()
                    sendEmail(content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("unable to send email")
            elif 'message' in query:
                user_name={
                    'Nick':'+91 7975471268'
                }
            
                try:
                    speak("To Whom you want to send the watsapp message?")
                    name= takeCommandMic()
                    phone_no = user_name[name]
                    speak("What is the message?")
                    message=takeCommandMic()
                    sendwhatsmsg(phone_no,message)
                    speak("Whatsapp Message Has beeen Sent")
                except Exception as e:
                    print(e)
                    speak("Unable to send the message")

            elif 'wikipedia' in query:
                speak('Searching On Wikipedia...')
                query = query.replace("Wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            
            
            elif 'search' in query:
                searchgoogle()

                
            elif 'youtube' in query:
                speak("what should i search for youtube")
                topic=takeCommandMic()
                pywhatkit.playonyt(topic)

            elif 'weather' in query or 'climate' in query:
                city='bangalore'
                url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=d916f738b8c56aa3b5180f0625025c35'
                res=requests.get(url)
                data=res.json()
                weather=data['weather'][0]['id']
                temp=data['main']['temp']
                desp=data['weather'][0]['description']
                temp=round((temp-32)*5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f'weather in {city} city is like')
                speak('Temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))

            elif 'news' in query:
             
                try:
                    jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=ce6e2cf8d71a4ef78cdc8cefe6f3b286''')
                    data = json.load(jsonObj)
                    i = 1
                    
                    speak('here are some top news')
                    print('''=============== TIMES OF INDIA ============'''+ '\n')
                    
                    for item in data['articles']:
                        
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:
                    print(str(e))
            
            elif 'read' in query:
                text2speech()
            
            # elif 'covid' in query:
            #     jsonObj = urlopen('https://coronavirus-19-api.herokuapp.com/all') 
            #     data = json.load(jsonObj)
                
            #     i = 1
                    
            #     speak('Covid Updates')
                    
                    
            #     for item in data['data']:
                        
            #         print(str(i) + '. ' + item['deaths'] + '\n')
            #         print(item['cases'] + '\n')
            #         speak(str(i) + '. ' + item['Recovered'] + '\n')
            #         i += 1
                
            elif 'lock' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))

            elif ' code' in query:
                codepath='C:\\Users\\91829\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.8'            
                os.startfile(codepath)
                
            elif 'joke' in query:
                speak(pyjokes.get_joke())
            
            elif 'screenshot' in query:
                screenshot()
                
            elif 'remember' in query:
                speak("what should i remember?")
                data= takeCommandMic()
                speak("you asked me to remember that"+data)
                remember =open('data.txt','w')
                remember.write(data)
                remember.close()
            
            elif 'know' in query:
                remember=open('data.txt','r')
                speak("you told me to remember that"+remember.read())

                
            elif 'password' in query:
                passwordgen()  
    
            elif 'stackoverflow' in query:
                speak("Here you go. Happy coding")
                wb.open("https://stackoverflow.com")

            elif 'stack overflow' in query:
                speak("Here you go. Happy coding")
                wb.open("https://stackoverflow.com")

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you?")

            elif 'cpu' in query:
                cpu()
            
            elif 'shut down' in query:
                speak("Hold On! Your system is shutting down")
                subprocess.call('shutdown / p /f')
            
            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])
                

            elif 'made' in query:
                speak("TEAM Optimize Prime - For REVA Hack 2021")
                print("TEAM Optimize Prime - For REVA Hack 2021")

            elif 'goodbye' in  query:
                speak("Jack logging off")
                speak("thank you for giving me your time")
                quit() 
