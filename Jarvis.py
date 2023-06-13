import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# covert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis, sir please tell me how can i help you")

 # to Send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('engichoudjary@gmail.com', '#Mission123')
    server.sendmail('akshayrikk@gmail.com', to, content)
    server.close()





if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for task

        if "open notepad" in query:
            npath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(500)
                if k==200:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            speak(results)
            #print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+917309320243","chul bnd ho gyi kya bhaiya ji",2,25)
            speak("message send succesfully")

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "email to akshay " in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "engichoudjary@gmail.com"
                sendEmail(to,content)
                speak("Email has sent to akshay")

            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to sent this mail to akshay")

        elif "no thanks" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()

        speak("sir, do you have any other work")











