from Brain.AIBrain import ReplyBrain
# from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print("")
print(">> Starting The Jarvis : Wait for some Seconds.")
from Body.Speak import Speak
from Feature.Clap import Tester
print("")
print(">> Starting The Jarvis : Wait for few Seconds more...")
print("")
from Main import MainTaskExecution

def MainExecution():

    Speak("hello Sir!")
    Speak("I'm Jarvis, I'm Ready to assist you sir.")

    while True:
 
        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)

        if ValueReturn == True:
            pass
        
        elif len(Data)  < 3:
            pass

        elif "turn on the tv" in Data: # specific command ans is describe here
            Speak("Ok Sir... Turning on the tv")

        elif "call mummy ji" in Data: # specific command ans is describe here
            Speak("Ok Sir... wait for 3 seconds calling mummy ji")

        # elif "what is" in Data or "where is" in Data or "how many" in Data or "how" in Data or "question" in Data or "answer" in Data:
        #     Reply = QuestionsAnswer(Data)
        #     Speak(Reply)
        
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()