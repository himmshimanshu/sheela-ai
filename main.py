print("")
print("")
print("[Starting Sheela....., Please Hold For A Moment]")
print("")
print("")
import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup
import keyboard
import os
from time import sleep
import pyautogui
import random
from plyer import notification
from pygame import mixer
print("")
print("Preparing listen Function.....")
import speedtest
import volume
from volume import volumeup
from volume import volumedown
from SearchEngine import searchGoogle
print("")
print("Testing Your Microphone.......")
from SearchEngine import searchYoutube
from Translator import translation
from SearchEngine import searchWikipedia
from News import latestnews
from calculator import Calc
from Whatsapp import sendMessage
from Wakeup import wishMe
from speak import speak
from listen import micexecute
from AIBrain import Replybrain
import webview



for i in range(3):
    a = input("Enter Password to open Sheela :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("PASSWORD VERIFIED >>>>> WELCOME SIR!!!! PLZ SPEAK >>WAKE UP<< OR >>SHEELA<< TO CONTINUE")
        speak("PASSWORD VERIFIED. WELCOME SIR, Please SPEAK, WAKE UP OR , SHEELA TO CONTINUE")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

        #import gui from gui.py
def alarm(query):
    query = micexecute()
    query = str(query)
    timehere = open("Alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = micexecute()
        query = str(query)

        if "wake up" in query or "sheela" in query or "makeup" in query:
            wishMe()

            while True:
                query = micexecute()
                query = str(query)
                Datalen = len(query)

                if int(Datalen)<=1:
                    pass

                elif "go to sleep" in query or "sleep" in query:
                    speak("Going in Sleep Mode But You can call me anytime")
                    break 

                elif "change password" in query:
                    speak("Please Input The New Password")
                    new_pw = input("Enter The New Password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = []
                    speak("Want to clear old tasks (Please speak YES or NO)")
                    query = micexecute()
                    query = str(query)

                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("How Many Tasks You Want To Enter[NUMERIC FORM] :- "))
                        z = 0
                        for z in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{z}. {tasks[z]}\n")
                            file.close()
                    elif "no" in query:
                        z = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for z in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{z}. {tasks[z]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "translate" in query:
                    query = query.replace("Sheela","")
                    query = query.replace("translate","")
                    translation(query)

                elif ".com" in query or ".co.in" in query or ".org" in query:
                    speak("Opening In Browser , Sir")
                    query = query.replace ("open","")
                    query = query.replace("sheela","")
                    query = query.replace("launch","")
                    query = query.replace(" ","")
                    webbrowser.open(f"https://www.{query}")

                elif "launch" in query or "open" in query:
                    speak("Launching sir...")
                    query = query.replace ("open","")
                    query = query.replace("sheela","")
                    query = query.replace("launch","")
                    query = query.replace(" ","")
                    pyautogui.press('win')
                    sleep(1)
                    keyboard.write(query)
                    sleep(1)
                    keyboard.press('enter')
                    sleep(0.5)
                    
                elif "one tab" in query or "1 tab" in query:
                    pyautogui.hotkey("ctrl","w")
                    speak("Closed,sir")

                elif "2 tab" in query or "two tab" in query:
                    pyautogui.hotkey("ctrl","w")
                    sleep(0.5)
                    pyautogui.hotkey("ctrl","w")
                    speak("Closed,sir")

                elif "my internet speed" in query:
                    print("Checking Internet Speed !!!! <<WAIT FOR A WHILE>>")
                    print("Checking Internet Speed, WAIT FOR A WHILE")
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576   
                    download_net = wifi.download()/1048576
                    print("Your Download Speed is",download_net)
                    print("Your Upload speed is ",upload_net)
                    speak(f"Your Download speed is {download_net}")
                    speak(f"Your Upload speed is {upload_net}")
 #error in Ipl Function                   
                #elif "ipl score" in query or "cricket score" in query:
                #    url = "https://www.cricbuzz.com/"
                 #   page = requests.get(url)
                 #   soup = BeautifulSoup(page.text,"html.parser")
                 #   team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                 #   team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                 #   team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                 #   team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
                 #   a = print(f"{team1} : {team1_score}")
                  #  b = print(f"{team2} : {team2_score}")
                 #   a = speak(f"{team1} : {team1_score}")
                 #   b = speak(f"{team2} : {team2_score}")

                 #   notification.notify(
                 #       title = "CRICKET CURRENT SCORE :- ",
                 #       message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                 #       timeout = 40
                 #   )

                elif "screenshot" in query:
                     im = pyautogui.screenshot()
                     im.save("screenshot.jpg")

                elif "click my photo" in query:
                    pyautogui.press("win")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(15)
                    speak("Smile Please")
                    pyautogui.press("enter")

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("That's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "sheela" in query or "shila" in query:
                    speak("Yes sir, How may i help you")
                
                elif "play music" in query:
                    speak("Playing your favourite songs, sir")
                    webbrowser.open("https://www.youtube.com/watch?v=A_huhqaSLlM&list=RDA_huhqaSLlM")
                    
                

                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYoutube(query) 
                elif "wikipedia" in query:
                    searchWikipedia(query) 
                elif "amazon" in query:
                    speak("opening amazon")
                    webbrowser.open("www.amazon.com")
                elif "facebook" in query or "fb" in query:
                    speak("opening facebook")
                    webbrowser.open("www.facebook.com")
                elif "instagram" in query:
                    speak("opening instagram")
                    webbrowser.open("www.instagram.com")
                elif "flipkart" in query:
                    speak("opening flipkart")
                    webbrowser.open("www.flipkart.com")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    speak("Turning volume down")
                    volumedown()

                elif "news" in query:
                    latestnews()

                elif "calculate" in query:
                    query = query.replace("calculate","")
                    query = query.replace("sheela","")
                    Calc(query)

                elif "whatsapp" in query:
                    sendMessage()

                elif "temperature" in query:
                    search = "temperature in motihari"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in motihari"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("Input Time Example:- 10 and 10 and 10")
                    speak("Please Set The Time")
                    h = input("Please tell the time :- ")
                    alarm(h)
                    speak("Done,sir")
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "shutdown" in query or "shut down" in query:
                    speak("Shutting Down, sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("sheela","")
                    speak("You told me"+rememberMessage)
                    remember = open("remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt","r")
                    speak("You told me" + remember.read())

                elif "shutdown system" in query:
                    speak("Are You sure to shutdown the system")
                    shutdown = input("Do you wish to shutdown your computer? [yes/no]")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                
                else:
                    Reply = Replybrain(query)
                    speak(Reply)
