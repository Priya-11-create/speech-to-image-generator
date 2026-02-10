import os
import speech_recognition as sr
import requests
import webbrowser
from deep_translator import GoogleTranslator

# 🔑 Load Unsplash Access Key from Environment Variable
access_key = os.getenv("UNSPLASH_ACCESS_KEY")

if not access_key:
    print("Error: Please set your UNSPLASH_ACCESS_KEY environment variable.")
    exit()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    # 🎤 Speech to Text
    text = recognizer.recognize_google(audio)
    print("Original Speech:", text)

    # 🌍 Translate to English
    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    print("Translated to English:", translated_text)

    # 🖼 Fetch image from Unsplash
    url = f"https://api.unsplash.com/photos/random?query={translated_text}&client_id={access_key}"

    response = requests.get(url)
    data = response.json()

    if "urls" in data:
        image_url = data["urls"]["regular"]
        webbrowser.open(image_url)
    else:
        print("No image found for:", translated_text)

except Exception as e:
    print("Error:", e)

