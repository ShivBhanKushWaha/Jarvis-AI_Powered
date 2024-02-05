import speech_recognition as sr
import os

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)  # Listening mode har 8 sec bad sunega
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en')
    
    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def WakeUpDetected():
    query = Listen().lower()

    if "wake up" in query:
        # pass
        print("wake up is detected")
        # os.startfile(r"D:\6th semester\Jarvis\Main.py")

    else:
        pass

while True:
    WakeUpDetected()

