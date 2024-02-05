import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def openExe(Query):

    Query = str(Query).lower()

    if "visit" in Query:
        NameofWeb = Query.replace("visit ","")
        Link = f"https://www.{NameofWeb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        NameofWeb = Query.replace("launch ","")
        Link = f"https://www.{NameofWeb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    # elif "start" in Query:
    #     nameoftheapp = Query.replace("start ","")
    #     if "chrome" in nameoftheapp:
    #         os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    #         return True
        
        # elif "ohter file" in nameoftheapp:
        #     os.startfile(r"other file")
        #     return True
        # pyautogui.press('win')
        # sleep(1)
        # keyboard.write(nameoftheapp)
        # sleep(1)
        # keyboard.press('enter')
        # sleep(0.5)
        # return True

# openExe("launch youtube")