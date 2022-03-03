from time import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    Year = datetime.datetime.today().year
    Month = datetime.datetime.today().month
    Day = datetime.datetime.today().day
    speak("The current day is")
    speak(Day)
    speak(Month)
    speak(Year)

def wishme():
    speak("Welcome Back Vaibhav!")
    time_()
    date_()

    hour = datetime.datetime.today().hour

    if hour>=6 and hour<=12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<=24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service.Please tell me how can I help you today?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8#Represents the minimum length of silence (in seconds) that will register as the end of a phrase. Can be changed.Smaller values result in the recognition completing more quickly, but might result in slower speakers being cut off.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-Us')
        print(query)
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('bhajankavaibhav@gmail.com','vaibhav@123')
    server.sendmail('bhajankavaibhav@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    # wishme()

    while True:

        query = takeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,3)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content=takeCommand()
                speak('Who is the receiver?')
                receiver = input("Enter receiver's email:")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak('Unable to send mail!')

        elif 'search in chrome' in query:
            speak('What should I search?')
            chromepath = 'C:/Users/User/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            search=  takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search youtube' in query:
            speak('What should I search?')
            search_term = takeCommand().lower()
            speak('Here we go to YOUTUBE')
            wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif 'search google' in query:
            speak('What should I search?')
            search_term = takeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()
        
        elif 'go offline' in query:
            speak('Going offline sir!')
            quit()

        elif 'word' in query:
            speak('Opening MS Word...')
            ms_word = r'C:\Program Files\Microsoft Office\Office15\WINWORD.exe'
            os.startfile(ms_word)