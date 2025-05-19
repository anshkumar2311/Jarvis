import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import tempfile

def speak(text):
    if text.strip() == "":
        print("Nothing to speak.")
        return
    try:
        tts = gTTS(text=text, lang='en')
        # Use a temporary file to save the speech
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            temp_path = fp.name
            tts.save(temp_path)
            playsound(temp_path)
    except Exception as e:
        print(f"Error in speaking: {e}")

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Adjusting for ambient noise, please wait...')
        r.adjust_for_ambient_noise(source, duration=1)
        print('Listening...')
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
    except Exception as e:
        print(f"Error during recognition: {e}")
        return ""

if __name__ == "__main__":
    text = takecommand()

    if text:
        speak(text)
    else:
        print("No valid input detected to speak.")
