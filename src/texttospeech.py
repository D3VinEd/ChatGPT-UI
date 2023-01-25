import pyttsx3
from configparser import ConfigParser

def text_to_speech(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

