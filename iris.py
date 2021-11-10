import pyttsx3 
import datetime
import speech_recognition as sr
import smtplib
from secrets import senderemail,epwd,to
import webbrowser



engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices=engine.getProperty('voices')
    #print(voices[1].id)
    if voice==1:
        engine.setProperty('voice',voices[0].id)
        speak("hello this is Iris")

    if voice==2:
        engine.setProperty('voice',voices[1].id)
        speak("hello this is NYX")
    

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
    speak("Welcome back !")
    time()
    date()
    greeting()
    speak("Iris at your service, please tell me how can i help you?")

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
        print("Recognizing...") 
        query = r.recognize_google(audio , language="en-IN")
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


if __name__=="__main__":
    getvoices(2)
    wishme()
    while True:
        query = takeCommandMic().lower()
        
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

        elif 'see you' in query:
            quit() 
