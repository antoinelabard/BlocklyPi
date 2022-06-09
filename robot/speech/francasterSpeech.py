import speech_recognition as sr
import os
import random
from gtts import gTTS
import pygame
import time
import webbrowser


def answer(a=""):
    if a == "":
        a = record_audio("recording...")
    if "comment tu t'appelle" in a:
        francaster_speak("je m'appelle francaster")
    if "quelle heure est-il" in a:
        francaster_speak(time.strftime("%H:%M"))
    if "on est quel jour" in a:
        today = time.strftime("%A")
        print(today)
        if today == "Sunday":
            today = "dimache"
        elif today == "Monday":
            today = "lundi"
        elif today == "Tuesday":
            today = "mardi"
        elif today == "Wednesday":
            today = "mercredi"
        elif today == "Thursday":
            today = "jeudi"
        elif today == "Friday":
            today = "vendredi"
        elif today == "Saturday":
            today = "samedi"
        francaster_speak(today)
    if "recherche" in a:
        francaster_speak("Que chcerchez-vous ?")
        search = record_audio("recording...")
        url = "https://google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        print("Voilà ce que j'ai trouver pour {}".format(search))
    if "trouve une adresse" in a:
        location = record_audio("vous voulez rechercher quoi?")
        url = 'https://www.google.fr/maps/place/' + location + '/'
        webbrowser.get().open(url)
        francaster_speak("Voilà ce que j'ai trouvé")
        print("Voilà ce que j'ai trouvé pour {}".format(location))

    if "stop" in a:
        francaster_speak("À bientôt")
        exit()


def record_audio(ask=False, lang='fr'):
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        if ask:
            print(ask)
        audio = recognizer.listen(source, timeout=10)
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            francaster_speak("Désolé je n'ai pas compris")
        except sr.RequestError:
            francaster_speak("Une erreur c'est produite")
        return voice_data


def francaster_speak(audio_string, lang='fr'):
    pygame.mixer.init()
    print(audio_string)
    audio_string = audio_string
    tts = gTTS(text=audio_string, lang=lang)
    r = random.randint(1, 1000)
    audio_file = "file-" + str(r) + ".mp3"
    tts.save(audio_file)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    time.sleep(0.25)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    os.remove(audio_file)


def francaster_repeat(lang='fr'):
    a = record_audio("recording...", lang=lang)
    francaster_speak(a, lang=lang)
