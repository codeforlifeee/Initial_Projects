import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Initialize the recognizer, translator, and TTS engine
recognizer = sr.Recognizer()
translator = Translator()
engine = pyttsx3.init()

def translate_speech(source_language='hi', target_language='en'):
    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        # Recognize speech using Google Speech Recognition
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=source_language)
        print(f"Original Text: {text}")
        
        # Translate text to the desired language
        translated = translator.translate(text, src=source_language, dest=target_language)
        translated_text = translated.text
        print(f"Translated Text: {translated_text}")
        
        # Convert translated text to speech
        engine.say(translated_text)
        engine.runAndWait()
    
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, there was an issue with the request.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with desired source and target language codes
translate_speech(source_language='en', target_language='hi')  # Change 'en' and 'hi' as needed