# Speak Function - Two Speak Function

# Window Based - pip install pyttsx3
# Chrome Based - pip install selenium==4.1.3

# Window Based
# Fast and Offline Advantage
# Overspeak and lessVoices Dis Adv.

# import pyttsx3

# def Speak(Text):
    # eengine = pyttsx3.init("sapi5")
    # voices = eengine.getProperty('voices')
    # eengine.setProperty('voices',voices[1].id)
    # eengine.setProperty('rate',170)
    # print("")
    # print(f"You : {Text}")
    # eengine.say(Text)
    # eengine.runAndWait()

# Speak("Hello I am shivbhan ")

# Chrome Based
# Adv more voices , more clear Over speaking
# Dis Adv. Word limit , Slow..

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
# chrome_options.headless = False # chrome open hokr dikhega
chrome_options.headless = True
Path = "Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):

    lengthOfTExt = len(str(Text))

    if lengthOfTExt ==0:
        pass

    else:
        print("")
        print(f"Jarvis :- {Text}")
        print("")
        data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()

        if lengthOfTExt>=30:
            sleep(4)
        
        elif lengthOfTExt>=40:
            sleep(6)
        
        elif lengthOfTExt>=55:
            sleep(8)

        elif lengthOfTExt>=70:
            sleep(10)

        elif lengthOfTExt>=100:
            sleep(12)

        elif lengthOfTExt>=120:
            sleep(14)

        else:
            sleep(2)

# Speak("Hello I am shivbhan Kushwaha")