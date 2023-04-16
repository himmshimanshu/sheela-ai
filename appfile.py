import pyautogui
import webbrowser
from speak import speak
from time import sleep
import keyboard


usefulapp = {"commandprompt":"cmd","Notepad":"notepad","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpoint"}
def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("sheela","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        appname = query.replace("start","")
        appname = query.replace("launch","")
        appname = query.replace(" ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(appname)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)

def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
        
    else:
        pyautogui.hotkey("alt","f4")
        speak("Closing The App, Sir....")  
