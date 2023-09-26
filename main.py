from moviepy.editor import VideoFileClip

# Открываем видеофайл
video = VideoFileClip("tt.mp4")

# Извлекаем аудио из видео
audio = video.audio

# Сохраняем аудио в файл
audio.write_audiofile("output.wav")

import speech_recognition as sr

# Создаем объект распознавания речи
r = sr.Recognizer()

# Загружаем аудиофайл
filename = "output.wav"

# Открываем и читаем аудиофайл
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language='ru-RU')
    print(text)