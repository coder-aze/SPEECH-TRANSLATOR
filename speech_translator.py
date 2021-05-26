import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import random
from google_trans_new import google_translator  

class Speech_Translator:
    def __init__(self,target_lang):
        self.target_lang=target_lang
        self.r=sr.Recognizer()

    def Translator(self,sentence):
        translator=google_translator()
        translated_thing=translator.translate(sentence,lang_src="en",lang_tgt=self.target_lang)
        return translated_thing

    def speech_to_text(self):
        test=sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk")
            audio=test.listen(source)
            current_text=test.recognize_google(audio)
            print("Your say it: "+current_text)
            print("Translated version: "+self.Translator(current_text))
            txttospeech=gTTS(text=self.Translator(current_text),lang=self.target_lang)

            filename="audio"+str(random.randint(1,100000000))+".mp3"
            txttospeech.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

while True:
    select_lang=str(input("choose language  or  exit-1: "))
    if select_lang==1:
        break
    while True:
        test=Speech_Translator(select_lang)
        test.speech_to_text()
        try_again=int(input("1-Try Again\n2-Stop: "))
        if try_again==1:
            continue
        else:
            break