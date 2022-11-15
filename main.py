import os
import pyttsx3  # THIS MODULE CONVERT THE TEXT INTO AUDIO

import speech_recognition as sr
import wikipedia  # this module will help us for searching on wikipedia
import webbrowser # this module will help in opening differnt sites on web browser



engine =pyttsx3.init('sapi5')  # we use this for using the inbuilt voices of the window
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)   # setting voices 


def speak(audio):
    '''
      this speak function will convert the given text into audio
      means what parameter it get it will speak out
    '''
    engine.say(audio)    #say function will convert the given text into audio 
    engine.runAndWait()

def takeCommand():
    '''
       it takes the microphone input feom the user and returns the string output
    '''
    r=sr.Recognizer()  #  Recognizer class will help to recognize the audio of user 
    with sr.Microphone() as source:
        r.pause_threshold=1     # pause_threshold vo attribute jo decide krega ki ham agr 1 sec nhi bole to vo program ko terminate kr dega 
                                #seconds of non-speaking audio before a phrase is considered complete
        
        audio=r.listen(source)  # this will listen our audio 

    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')  # this will convert user audio (whic is command) into text 
    except Exception as e:
        # print("Error",e)
        print("PLease say that again")
        return "None "
    
    return query



if __name__=="__main__":
    speak("Hello sir How can i help you")
    while True:
         query=takeCommand().lower()

         # logic for executing task base don query
        
         if 'wikipedia' in query:
            speak("searching on wikipedia ")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2) # this function will return the details in 2 sentence from searching on wikipedia
            speak("According to wikipedia")
            speak(result)
        
         elif 'open youtube' in query:
            webbrowser.open("youtube.com")   # this function will open the website provided th elink as argument
        
         elif 'open google' in query:
            webbrowser.open("google.com")

         elif 'open facbook' in query:
            webbrowser.open("facebook.com")

         elif "open stackowerflow " in query:
            webbrowser.open('stackowerflow.com')

         elif "play music" in query:
             music_dir=""
             songs=os.listdir(music_dir) # this function of os module will return all the songs present in our directry
             os.startfile(os.path.join(music_dir,songs[0]))  

         elif "open vs code" in query:
            os.startfile("C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")  #  os.startfile this function will open the  given file

         
     