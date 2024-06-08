from gtts import gTTS
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition

class Speech_Recognition:
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
        

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        return audio

    def unknownface(self):
        audio = "UNKNOWN PERSON"
        language = "en"
        for i in range(1,6):
            self.speak(audio)
        speech = gTTS(text=audio, lang=language, slow=False)
        

    def submit(self):
        audio = "Your Status Has Been Recorded"
        language= "en"
        speech = gTTS(text=audio, lang=language, slow=False)
        self.speak(audio)

