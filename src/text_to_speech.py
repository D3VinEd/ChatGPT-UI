import pyttsx3
from configparser import ConfigParser


def text_to_speech(text) -> None:
    config = ConfigParser()
    config.read('config/config.ini')
    engine = pyttsx3.init()
    engine.setProperty('rate', config['SPEECH']['speed'])
    engine.say(text)
    engine.runAndWait()

