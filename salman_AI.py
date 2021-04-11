import pyttsx3 # pip install
import speech_recognition as sr # pip install speechRecognize
import webbrowser
import datetime
import wikipedia # pip install wikipedia
import os
import smtplib


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Evening  Salman sir  ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Salman sir")

    else:
        speak("Good Morning Salman sir")

    speak("i am jarvis  sir , please tell how may i help you !!!")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone()  as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing..")
            query=r.recognize_google(audio , language="en-in")
            print(f"User Said:{query}")

        except Exception as e:
            print("Say That Again Please....")
            return 'None'
        return query

def sendEmail(to , content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail@gmail.com' , 'yourPassword') # !!!!!!! Security Alert !!!!!!!!!!
    server.sendmail('yourEmail@gmail.com' , to , content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:

        # Logic for executing tasks based on query
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace('wikipedia' ,"")
            results=wikipedia.summary(query , sentences=2)
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'How are you' in query:
            speak("im fine sir with your pleasure")

        elif 'play music' in query:
            music_dir="D:\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is: {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\ELCOT\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm ' in query:
            pyPath="C:\Program Files\JetBrains\PyCharm Community Edition 2020.3.3\bin\pycharm64.exe"
            os.startfile(pyPath)

        elif ' email to sanjay'  in query:
            try:
                speak("What should i say ?")
                content=takeCommand()
                to="yourfriendemail@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry my friend salman , i am not able to send this email at this time ")