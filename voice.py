import pyttsx3
from pydub import AudioSegment
import re



def engine_settings(engine, article_languge):
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 185) # Выставляем скорость чтения голоса
    for voice in voices:
        if voice.languages == article_languge and \
                voice.gender == 'VoiceGenderMale':
            return engin.setProperty('voice', voice.id) # Выбкраем подходящий голос


def get_mp3_file(file_name, article_text, article_language):
    engine = AudioSegment
    engine_settings(engine, article_language)  # Применение настроек голоса
    engine.save_to_file(article_text, file_name)  # Сохраняем текст статьи в аудифайл
    engine.runAndWait()
    convert_file_to_mp3(file_name)  #Конвертация в mp3 формат



def convert_file_to_mp3(file_name):
    convert = AudioSegment
    convert_file = convert.from_file(file_name)
    convert_file.export(file_name, format="mp3")


def get_file_name(link):
    # Название файла - ссылка на статью
    file_name = re.split(r'^https?:\/\/?', link)[1]
    for symbols_in_file_name in ['/', '.', '_']:
        # Замена символов в названии файла на _, чтобы сохранить файл в ОС
        file_name = file_name+'.mp3' # сохраняем файл изначально в мр3 формате
        return file_name

