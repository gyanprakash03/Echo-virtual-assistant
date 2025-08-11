import speech_recognition as sr
import pyttsx3
import webbrowser
# from links import links
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv
import pyautogui
import pyperclip
import pygetwindow as gw


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

general_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", 
    system_instruction="You are a virtual assistant. Your name is Echo. Keep your responses short and concise and be friendly. If you don't know the answer, say 'I don't know'. Don't use any special characters or emojis in your responses. if asked for link of a website or song, provide the link in the format 'https://www.example.com'. If you don't have a link, say 'I don't have a link for that'.",
)

whatsapp_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", 
    system_instruction=(
        "Suppose you are a Gyan i.e., Me. i am a coder and a college student. your job is to analyze a whatsapp chat history that i provide you and respond to the lastest message just like how i would respond in first person. You just need to provide the next response in plain text format, using emoji if required in that context"
    )
)

def ask_gemini(model, prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Sorry, I can not answer that right now."


def handle_whatsapp():
    for w in gw.getAllWindows():
        if "WhatsApp - Google Chrome" in w.title:
            w.minimize()
            w.restore()
            w.activate()
            break
    time.sleep(0.5)

    pyautogui.moveTo(718, 247)
    pyautogui.mouseDown()

    pyautogui.moveTo(1390, 1048, duration=0.5)
    pyautogui.mouseUp()

    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(683, 759)

    chat_text = pyperclip.paste()

    reply = ask_gemini(whatsapp_model, f"Respond to this WhatsApp message: {chat_text}")

    pyperclip.copy(reply)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")


recog = sr.Recognizer()

def speak(text):
    print(f"Echo: {text}")
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.2) 


def listen(txt, suppress_sorry=False):
    with sr.Microphone() as source:
        # recog.adjust_for_ambient_noise(source, duration=1)
        print(txt)
        try:
            audio = recog.listen(source, timeout=5, phrase_time_limit=5)
            # print("Audio captured, recognizing...")
            command = recog.recognize_google(audio)
            print(f"User: {command}")

            if "echo" in command:
                speak("yes")
            return command.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            if not suppress_sorry:
                speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            speak("Sorry, my speech service is down.")
        return ""


def process_command(command):
        
    if command.startswith("open "):
        dest = command.replace("open", "", 1).strip()
        speak(f"Opening {dest}...")
        gemini_response = ask_gemini(general_model, f"give link for {dest} website")

        link = [word for word in gemini_response.split() if "https" in word]
        if link:
            webbrowser.open(link[0])
        else:
            speak("Sorry. I am unable to execute this request")

    elif command.startswith("play "):
        song = command.replace("play", "", 1).strip()
        speak(f"Playing {song}...")
        gemini_response = ask_gemini(general_model, f"give link for {song} song")

        link = [word for word in gemini_response.split() if "https" in word]
        if link:
            webbrowser.open(link[0])
        else:
            speak("Sorry. I am unable to execute this request")
    
    elif command == "hello":
        speak("Hello! How can I help you today?")

    elif "sleep" in command:
        print("\n")
        return "sleep"
    
    elif command.startswith("reply"):
        handle_whatsapp()

    else:
        print("Thinking...")
        gemini_response = ask_gemini(general_model, command)
        speak(gemini_response)

    print("\n")


def main():
    speak("Hi! I am Echo.")
    while True:
        command = listen("Echo is asleep", True)
        if "exit" in command:
            speak("Goodbye!")
            exit()

        if "echo" in command:
            print("\n")
            while command != "sleep":
                command = listen("listening...", False)
                if command:
                    process_command(command)

if __name__ == "__main__":
    main()
