from email.mime import audio
import speech_recognition

sr = speech_recognition.Recognizer()    #создание элемента обращения к библиотеке
sr.pause_threshold = 0.5

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source = mic, duration = 0.5)       #элемент получениия образа окружающего шума перед запуском
    audio = sr.listen(source = mic)     #элемент получения данных с микрофона устройства
    query = sr.recognize_google(audio_data = audio, language = 'ru-RU')     #переменная для записи, распознанной через google API, речи 
    query.lower()       #перевод всего распзнанного текста в нижний регистр
print(query)
