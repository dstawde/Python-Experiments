#python personal assistant
#pip install speechrecognition
#pip install pyaudio

import os
import datetime
import speech_recognition as sr
import webbrowser
from time import ctime
#import PyObjC
import random
from gtts import gTTS
import playsound
import subprocess
from selenium import webdriver

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source: 
        if ask:
            alexis_speak(ask)              
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('Sorry I did not get that')
        except sr.RequestError:
            alexis_speak('Sorry Speech Server is down')
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'jarvis-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('my name is Sunny Leone')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'who is the richest person' in voice_data:
        alexis_speak('Its sachin ')
    if 'find something' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.register('chrome',None,
	    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open_new(url)
        alexis_speak('here is what if found for ' + search)
    if 'open email' in voice_data:
        alexis_speak('opening your email')
        subprocess.call(["C:/Program Files (x86)/Mozilla Thunderbird/thunderbird.exe"])
    if 'open my email' in voice_data:
        alexis_speak('opening gmail')
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://gmail.com")
        driver.find_element_by_name("identifier").send_keys("dst062@gmail.com")
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
        driver.implicitely_wait(5)
        # above test is failing on next as chrome detects it as not secure


    if 'exit' in voice_data:
        exit()
    return respond

alexis_speak('How can I help you')
voice_data = record_audio()
respond(voice_data)







