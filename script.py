import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listen = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    command = ""  # Initialize command to avoid UnboundLocalError
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listen.listen(source)
            command = listen.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            print(command)
    except Exception as e:  # Catch specific exceptions and print for debugging
        print(f"Error recognizing speech: {e}")
    return command

def run_alexa():
    command = take_command()

    # Check if command is empty or None, and skip if no command is detected
    if not command:
        speak('I didn\'t catch that, please try again.')
        return

    print(command)
    
    if 'open' in command:
        song = command.replace('play', '')
        speak('opening ' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        speak(info)
    
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif "what is" in command:
        person = command.replace('what is', '')
        info = webbrowser.open(person)
        speak(info)
    else:
        speak('Please say the command again!')

        
while True:
    run_alexa()