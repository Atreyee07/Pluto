import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pluto' in command:
                command = command.replace('pluto', ' ')
                file_path = r"C:\Users\KIIT\Desktop\Myy Documents\Pycharm_Note\noted.txt"
                with open(file_path, 'a') as file:
                    print('file opened')
                    file.write(command + '\n')
                    print('writing file')
                file.close()
                print('file closed successfully')

    except Exception as e:
        print(e)
    return command
def run_pluto():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M %p')
         print(time)
         talk('Current time is ' +time)

    elif 'write' in command:
         talk('yes dictate me')
         try:
             with sr.Microphone() as source:
                 print('listening2....')
                 voice = listener.listen(source)
                 para = listener.recognize_google(voice)
                 para = para.lower()
                 if 'pluto' in para:
                     para = para.replace('pluto', ' ')
                     file_path = r"C:\Users\KIIT\Desktop\Myy Documents\Pycharm_Note\noted.txt"
                     with open(file_path, 'a+') as file:
                         print('file opened again')
                         file.write(para + '\n')
                         print('write file part2')
                     file.close()
                     print('file closed part2')

         except Exception as e:
             print(e)


    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 4)
        print(info)
        talk(info)

    elif 'date' in command:
         talk('sorry, I have a partner')

    elif 'joke' in command:
         talk(pyjokes.get_joke())

    else:
        talk('Sorry please say it again ')
#while True:
run_pluto()