import time
import keyboard
from PIL import ImageGrab
import requests
import os
import tempfile
import pyttsx3
import speech_recognition as sr
import winsound
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://localhost:8000/analyze"
TIMEOUT_DURATION = 60
SELECTED_MIC_ID = 8  


def get_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
  
    for voice in voices:
        if "english" in voice.name.lower() or "en" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break
            
    engine.setProperty('rate', 160) 
    engine.setProperty('volume', 1.0)
    return engine

def speak(text):
    try:
        engine = get_engine()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Voice Error: {e}")

def play_beep(frequency=1000, duration=200):
    try:
        winsound.Beep(frequency, duration)
    except:
        pass


def listen_to_user():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8
    r.dynamic_energy_threshold = True

    try:
        with sr.Microphone(device_index=SELECTED_MIC_ID) as source:
            print(f"\n [MIC {SELECTED_MIC_ID}] ACTIVATED! Adjusting for noise...")
            r.adjust_for_ambient_noise(source, duration=0.8)
            
            print("SPEAK NOW, BOSS! (Wait for the beep)")
            play_beep(800, 200)

            audio = r.listen(source, timeout=5, phrase_time_limit=15)
            
            play_beep(500, 200)
            print(" Processing speech...")
            

            text = r.recognize_google(audio, language="en-US")
            print(f"HEARD: '{text}'")
            return text

    except OSError:
        print(f"ERROR: Microphone ID {SELECTED_MIC_ID} not found!")
        return None
    except sr.WaitTimeoutError:
        print("No speech detected.")
        return None
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except Exception as e:
        print(f"Microphone Error: {e}")
        return None

def capture_and_analyze():
    print("\n Capturing screen...")
    screenshot = ImageGrab.grab()
    
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        screenshot.save(tmp_file.name)
        tmp_path = tmp_file.name

    user_prompt = listen_to_user()

    if not user_prompt:
        speak("I couldn't hear you, running a general visual analysis.")
        user_prompt = "What do you see on this screen? Explain the important details and propose a solution."

    print(f"Sending to Gemini: '{user_prompt}'")

    try:
        with open(tmp_path, "rb") as f:
            files = {"file": f}
            data = {"message": user_prompt}
            response = requests.post(API_URL, files=files, data=data, timeout=TIMEOUT_DURATION)

        os.remove(tmp_path)

        if response.status_code == 200:
            result = response.json()
            cevap = result.get("solution", "No response.")
            
            print("-" * 50)
            print(f"CORTEX: {cevap}")
            print("-" * 50)
            
            ilk_cumle = cevap.split('.')[0]
            speak(ilk_cumle)
            
        else:
            print(f"Server Error: {response.text}")
            speak("I encountered a server error, boss.")

    except Exception as e:
        print(f"Critical Error: {str(e)}")
        speak("A critical error occurred.")


if __name__ == "__main__":
    print(f"\nCORTEX ENGLISH VOICE ASSISTANT ONLINE (MIC ID: {SELECTED_MIC_ID})")
    print("👉 Hotkey: CTRL + ALT + S")
    
    speak("System is ready, boss. Awaiting your command.")
    
    keyboard.add_hotkey('ctrl+alt+s', capture_and_analyze)
    keyboard.wait()