import speech_recognition as sr
from easytello import tello 

drone = tello.Tello()

def audioRecognizer():
    speech = sr.Recognizer()
    text = ""
    #audio = ''

    with sr.Microphone() as source:
        print("say your command: ")
        audio = speech.listen(source,phrase_time_limit=3)
        #print("stop.")

        try:
            text = speech.recognize_google(audio,language="fr-FR")
            print("your command: ",text)
            #return text

        except:
            
            print("i'm waiting for your command.")
    return text


def action(input_command):
    
    if "démarre" in input_command:
        drone.land()

    elif "fermer" in input_command:
        drone.takeoff()
        
    elif "avant" in input_command:
        drone.forward(30)
        
    elif "haut" in input_command or "derrière" in input_command:
        drone.back(30)
        
    elif "droite" in input_command or "rye" in input_command:
        drone.right(30)
        
    elif "gauche" in input_command:
        drone.left(30)
        
    elif "va droite" in input_command:
        drone.cw(30)
        
    elif "va gauche" in input_command:
        drone.ccw(30)
        
    elif "monte" in input_command or "up" in input_command:
        drone.up(30)
        
    elif "descendez" in input_command or "descender" in input_command or "descend" in input_command:
        drone.down(30)


    else:
        pass


while True:
    
    text = audioRecognizer().lower()

    if text == 0 :
        continue

    if "bye" in str(text) or "see you later" in str(text):
        
        break

    action(text)


