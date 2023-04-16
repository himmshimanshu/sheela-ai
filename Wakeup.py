from speak import speak
import datetime

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("It's A Pleasent Morning, sir")
        print("It's A Pleasent Morning, sir!!!")

    elif hour >12 and hour<=18:
        speak("It's A Pleasent Afternoon, sir")
        print("It's A Pleasent Afternoon, sir!!!")

    else:
        speak("It's A Pleasent Evening, sir")
        print("It's A Pleasent Evening, sir!!!")

    speak("I Am Sheela, Your Personal Assistance Helps To Make Your Works Easier To Do")
    print("I Am Sheela, Your Personal Assistance Helps To Make Your Works Easier To Do")


