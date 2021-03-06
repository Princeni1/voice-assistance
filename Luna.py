import pyttsx3  #pip install pyttsx
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia                 #pip install wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening! ")
        
    speak("I an  Luna ! , your virtual assistent. how can I help You ?")
    
def takeCommand():
    #it takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

#def sendEmail(to, content):

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)   #sentence used for how much line you want Luna to read 
            speak("According To wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open youtube music' in query:
            webbrowser.open("music.youtube.com")
        
        elif 'play music' in query:
            webbrowser.open("https://music.youtube.com/watch?v=eFEEQwGLqT4&list=LM")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif 'email to prince' in query:
            try:
                speak("What should I say ?")
                content= takeCommand()
                to = "Princenishad420@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("sorry , I am not able to send this email.")
        
        elif 'close' in query:
            exit()              #to stop using you voice assistance otherwise it will keep listning

            
            #some time it show error as pyaudio is not install for that
            #first step write-    pip install pipwin
            # second step -       pipwin install pyaudio
         
        
