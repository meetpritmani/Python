import pyttsx3
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init('sapi5')  # Microsoft Speech api
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def yousaid():
    speak(text)


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You Said: ", text)
        yousaid()
    except:
        print("Please Try Again")
