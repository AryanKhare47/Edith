import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit as kit
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Edith Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'what is your name' in query:
            speak("My Name is edith. I am Mr. Aryan khare sir's personal Assistant")
        elif 'my name is ashu' in query:
            speak("Hello Ashu,nice to meet you. I have heard a lot about you . How is everything going")        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")   
        elif 'open opera' in query:
                npath="C:\\Users\\Aryan\\OneDrive\\Desktop\\Opera GX Browser.lnk"
                os.startfile(npath)
        elif 'open visual studio' in query:
            npath = "C:\\Users\\Aryan\\OneDrive\\Desktop\\Visual Studio Code.lnk" 
            os.startfile(npath) 
        elif 'play music youtube' in query:
            kit.playonyt("agar tum sath ho") 
        elif 'play fastly on youtube'in query:
            kit.playonyt("fassle")
        elif 'play kahani suno on youtube' in query:
            kit.playonyt("Kahani suno 2.0")   
        elif "no thanks" in query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()


        speak("do you have any other work")

                
