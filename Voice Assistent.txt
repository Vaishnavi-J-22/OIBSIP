import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening To you...!!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""


def main():
    speak("Hello! How can I assist you?")
    command = recognize_speech()
    while(1):
        if "hello" in command:
            speak("Hello there.. :)")
        elif "time" in command:
            speak(datetime.datetime.now().strftime("%I:%M %p"))
            print(datetime.datetime.now().strftime("%I:%M %p"))
        elif "date" in command:
            speak(datetime.datetime.now().strftime("%B %d, %Y"))
            print(datetime.datetime.now().strftime("%B %d, %Y"))
        elif "search" in command:
            speak("What do you want to search for?")
            query = recognize_speech()
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Sorry, I didn't understand that.")
            print("Sorry, I didn't understand that.")
        


if __name__ == "__main__":
    main()
