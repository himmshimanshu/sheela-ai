from listen import micexecute
from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans
from gtts import gTTS
import googletrans
from speak import speak
import os
from playsound import playsound
import time

query = micexecute()
query = str(query)

def translation(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")   
    text_to_translate = translator.translate(query,src = "auto",dest= b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")





