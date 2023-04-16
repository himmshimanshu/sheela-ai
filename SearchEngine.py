import webbrowser
from listen import micexecute
from speak import speak
import pywhatkit
import wikipedia
import wikipedia as googleScrap

query = micexecute()
query = str(query)

def searchGoogle(query):
    if "google" in query:
        
        query = query.replace("sheela","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("According To Google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)

        except:
            speak("Sorry Sir ,Nothing Found On Google")

def searchYoutube(query):
    if "youtube" in query:
        speak("Opening Your Result On Youtube")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("sheela","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Playing The First Video, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching {query} on Wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("sheela","")
        Results = wikipedia.summary(query,sentences = 3)
        speak("According To Wikipedia..")
        print(Results)
        speak(Results) 