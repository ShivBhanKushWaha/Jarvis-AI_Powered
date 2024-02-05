# hindi  or english - command 
# English me sunega 
# reply in english

# step 1
#pip install googletrans==3.1.0a0

# step 2 
# three function
# 1 - Listen
# 2 - English translation
# 3 - Connect

import speech_recognition as sr # pip install speech_recognition
from googletrans import Translator # pip install googletrans==3.1.0a0

# 1 - Listen

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)  # Listening mode har 8 sec bad sunega
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en')
    
    except:
        return ""
    
    query = str(query).lower()
    return query

# Listen()
# print(Listen())

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translator = Translator()
    result = translator.translate(line) # default english
    data = result.text
    print(f"You :- {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

# MicExecution()