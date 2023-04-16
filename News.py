import requests
import json
from speak import speak

def latestnews():
    api_dict = {"business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=70fc88131c104dfea82f480a3b15d2aa" ,
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=70fc88131c104dfea82f480a3b15d2aa",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=70fc88131c104dfea82f480a3b15d2aa",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=70fc88131c104dfea82f480a3b15d2aa",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=70fc88131c104dfea82f480a3b15d2aa",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=70fc88131c104dfea82f480a3b15d2aa"
}

    content = None
    url = None
    speak("What Type Of News You Want To Hear, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    print("What Type Of News You Want To Hear, business , health , technology , sports , entertainment , science ")
    field = input("Please Type Which Type Of News You Want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print("Here Is The News You Want")
            break
        else:
            url = True
    if url is True:
        print("Sorry to Find News Related To Your Choice")
        speak("Sorry to Find News Related To Your Choice")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is Your news, Sir")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"Visit For More: {news_url}")

        a = input(">>press 1 to continue<< and >>press 2 to stop<<")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
