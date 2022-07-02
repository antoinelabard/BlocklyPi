import requests
import speech_recognition as sr
import os
import random
from gtts import gTTS
import pygame
import time
import webbrowser
import datetime


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


def souhaite_moi():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        francaster_speak("Bonjour")
    elif 12 <= hour < 18:
        francaster_speak("Bon aprés midi")
    else:
        francaster_speak("Bonne nuit")


def answer(a=None):
    if a == None:
        a = record_audio("recording...")
    if "comment tu t'appelle" in a:
        francaster_speak("je m'appel francaster")

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
        francaster_speak("vous voullez rechercher quoi?")
        search = record_audio("recording...")
        url = "https://google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        print("Voila ce que j'ai trouver pour \t".format(search))

    if "trouve une adresse" in a:
        location = record_audio("vous voullez rechercher quoi?")
        url = 'https://www.google.fr/maps/place/' + location + '/'
        webbrowser.get().open(url)
        francaster_speak("Voila ce que j'ai trouver")
        print("Voila ce que j'ai trouver pour \t" + location)

    if "ouvre youtube" in a:
        webbrowser.open_new_tab("https://www.youtube.com")
        francaster_speak(" voila youtube")
        time.sleep(5)

    if "ouvre google" in a:
        webbrowser.open_new_tab("https://www.google.com")
        francaster_speak("Google chrome est ouvert")
        time.sleep(5)

    if "ouvre gmail" in a:
        webbrowser.open_new_tab("gmail.com")
        francaster_speak("Google Mail est ouvert")
        time.sleep(5)

    if "météo" in a:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        francaster_speak("vous voulez la méteo de quele ville")
        city_name = record_audio("recording ...")
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            francaster_speak(" Temperature en kelvin c'est " +
                             str(current_temperature) +
                             "\n humidité en percentage c'est " +
                             str(current_humidiy) +
                             "\n description  " +
                             str(weather_description))
            print(" Temperature en kelvin  = " +
                  str(current_temperature) +
                  "\n humidité (en percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
        else:
            francaster_speak(" ville non trouvé ")

    if "fabriquer par qui" in a or "qui t'as créer" in a:
        francaster_speak("c'est francas qui m'a dévloppé")
        print("c'est francas qui m'a dévloppé")

    if "qui es tu et a quoi tu sert" in a:
        francaster_speak(
            "Je m'appelle francaster. Je suis programmé à répondre à vos question et obéir à vos ordre Je sais ouvrir youtube,google,gmail. Je pourrais vous dire l'heure,prendre des capture d'ecran,rechercher sur wikipedia, je pourrais vous dire aussi la méteo du jours")

    if "stop" in a:
        francaster_speak("à bientot")
        exit()


print(sr.Microphone.list_microphone_names())
answer()
# souhaite_moi()
