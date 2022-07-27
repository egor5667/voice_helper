from email.mime import audio
import speech_recognition

sr = speech_recognition.Recognizer()    
sr.pause_threshold = 0.5

def greet():
    return("привет!")

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source = mic, duration = 0.5)     
    audio = sr.listen(source = mic)    
    query = sr.recognize_google(audio_data = audio, language = 'ru-RU')
    query = query.lower()

    
if query == "здравствуй":
    print(greet())
else:
    print("Ничего не понял!")
    print("Ты сказал: ", query)
