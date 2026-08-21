import speech_recognition as sr

r = sr.Recognizer()

def take_command():
    print("Listening...")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-IN")
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand.")
        return ""
    except sr.RequestError as e:
        print("API error:", e)
        return ""
