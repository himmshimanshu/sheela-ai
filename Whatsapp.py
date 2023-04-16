import pywhatkit
from speak import speak
import datetime
from datetime import timedelta
from datetime import datetime

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message?")
    a = int(input('''Bittu bhai - 1
    Vishal bhai - 2
    Vivek - 3
    Khusi - 4
    Didi - 5
    Aunty ji - 6
    Bhai - 7
    kunal - 8
    Swarnil - 9
    Shashank - 10
    Fua ji - 11
    Fufa ji - 12
    Bade - 13
    Pappu - 14'''))
    if a == 1:
        speak("What's the message sir")
        message = str(input("Enter Message To Bittu Bhai- "))
        pywhatkit.sendwhatmsg ("+917352409400",message,time_hour=strTime,time_min=update)
    elif a==2:
        speak("Whats the message")
        message = str(input("Enter Message To Vishal bhai- "))
        pywhatkit.sendwhatmsg ("+917492941796",message,time_hour=strTime,time_min=update)
    elif a==3:
        speak("Whats the message")
        message = str(input("Enter Message To Vivek- "))
        pywhatkit.sendwhatmsg ("+918969855817",message,time_hour=strTime,time_min=update)
    elif a==4:
        speak("Whats the message")
        message = str(input("Enter Message To Khusi- "))
        pywhatkit.sendwhatmsg ("+917870472212",message,time_hour=strTime,time_min=update)
    elif a==5:
        speak("Whats the message")
        message = str(input("Enter Message To Didi- "))
        pywhatkit.sendwhatmsg ("+919341544857",message,time_hour=strTime,time_min=update)
    elif a==6:
        speak("Whats the message")
        message = str(input("Enter Message To Aunty Ji- "))
        pywhatkit.sendwhatmsg ("+917004722537",message,time_hour=strTime,time_min=update)
    elif a==7:
        speak("Whats the message")
        message = str(input("Enter Message To Bhai- "))
        pywhatkit.sendwhatmsg ("+917461078287",message,time_hour=strTime,time_min=update)
    elif a==8:
        speak("Whats the message")
        message = str(input("Enter Message To Kunal- "))
        pywhatkit.sendwhatmsg ("+917766888859",message,time_hour=strTime,time_min=update)
    elif a==9:
        speak("Whats the message")
        message = str(input("Enter Message To Swarnil- "))
        pywhatkit.sendwhatmsg ("+917858819432",message,time_hour=strTime,time_min=update)
    elif a==10:
        speak("Whats the message")
        message = str(input("Enter Message To Shashank- "))
        pywhatkit.sendwhatmsg ("+918789355474",message,time_hour=strTime,time_min=update)
    elif a==11:
        speak("Whats the message")
        message = str(input("Enter Message To Phua Ji- "))
        pywhatkit.sendwhatmsg ("+916204945959",message,time_hour=strTime,time_min=update)
    elif a==12:
        speak("Whats the message")
        message = str(input("Enter Message To Fufa Ji- "))
        pywhatkit.sendwhatmsg ("+917482885661",message,time_hour=strTime,time_min=update)
    elif a==13:
        speak("Whats the message")
        message = str(input("Enter Message To Bade- "))
        pywhatkit.sendwhatmsg ("+917050856461",message,time_hour=strTime,time_min=update)
    elif a==14:
        speak("Whats the message")
        message = str(input("Enter Message To Pappu- "))
        pywhatkit.sendwhatmsg ("+918578075164",message,time_hour=strTime,time_min=update)
    else:
        pass