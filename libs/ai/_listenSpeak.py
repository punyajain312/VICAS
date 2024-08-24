import speech_recognition as sr
import pyttsx3
from NLP._ai import match
# needs pyaudio
engine = pyttsx3.init()

def say(str):
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(str)
    engine.runAndWait()
    engine.stop()


def listen(txt=''):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            # , timeout=20, phrase_time_limit=10
            say(f"{txt}, I am Listening ")
            audio = recognizer.listen(source, phrase_time_limit=4, timeout=10)
            text = recognizer.recognize_google(audio)
            say("You said: " + text)
            print(text)
            confirmation = listen("Say ok to confirm")
            match_yes=match([{'LOWER':'ok'}],confirmation)
            ok = 1 if match_yes else 0
            return text if ok else listen("I am listening")
        except sr.UnknownValueError:
            say("Please try again")
            return listen()
        except sr.WaitTimeoutError:
            say("Please say something")
            return listen()
        except sr.RequestError as e:
            say("Could not request results from Google Speech Recognition service. Try later")
            return ''

