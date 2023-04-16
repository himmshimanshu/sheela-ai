import speech_recognition as sr
from googletrans import Translator

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

def TranslationHintoEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You Said : {data}")
    return data

def micexecute():
    query = listen()
    data = TranslationHintoEng(query)
    return data