import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")

#sptext()

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

#speechtx('Hello')

if __name__== '__main__':

   #if "hello google" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is Zira"
                speechtx(name)

            if "how are you" in data1:
                health = "i am fine, what about you."
                speechtx(health)
            
            elif "your age" in data1:
                age = " I am 20 years old"
                speechtx(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language='en',category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif "exit" in data1:
                speechtx("thank you")
                break


                    
    #else:
       #print("Thanks")