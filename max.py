import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from playsound import playsound
import os

engine = pyttsx3.init('sapi5')  # Microsoft Speech Api
voices = engine.getProperty('voices')

# print(voices[0].id) //DAVID
# print(voices[1].id) //Zira

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir...")
    elif hour >= 12 and hour < 15:
        speak("Good Noon Sir...")
    elif hour >= 15 and hour < 17:
        speak("Good Afternoon...")
    elif hour >= 17 and hour <=3:
        speak("Good Evening...")
    speak("Hello I am Maxy. How Can I Help You Sir")


def myspeech():
    # It Recognises my speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Gap Between Words
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # English India (en-in)
        print("Sir, You said: ", query)
    except Exception as e:
        print(e)  # if you Dont Want to Remove it
        a = "Sorry Sir Can You Repeat it"
        print("Sorry Sir Can You Repeat it")
        speak(a)
        return "None"
    return query


if __name__ == "__main__":
    greeting()

    while True:
        query = myspeech().lower()  # recognizing should be in lower case
        # My Logic For myspeech()

        if 'wikipedia' in query:
            speak('Searching For Wikipedia Please Wait')
            query = query.replace("wikipedia", "")
            answer = wikipedia.summary(query, sentences=1)
            speak("Sir, See What I Found")
            print(answer)
            speak(answer)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open shree chandra computers' in query:
            webbrowser.open("shreechandra.com")

        elif 'open w3schools' in query:
            webbrowser.open("w3schools.com")

        elif 'open dialer' in query:
            webbrowser.open("dialer.shreechandra.com")

        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'play music' in query:
            playsound('iphone-ringtone-trap-remix-mp3-128k-48521.mp3')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The time is {strTime}")

        elif 'open pycharm' in query:
            pycharmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.4\\bin\\pycharm64.exe"
            os.open(pycharmpath)