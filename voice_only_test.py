import speech_recognition as sr

r = sr.Recognizer()

print("Testing microphone... Speak now.")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("SUCCESS. You said:", text)
except Exception as e:
    print("FAILED:", e)
