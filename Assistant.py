import speech_recognition as sr
import pyttsx3

class Assistant():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.activationWord = 'tell, what, say, assistant'
    def speak(self, text, rate=160):
        self.engine.setProperty('rate', rate)
        self.engine.say(text)
        self.engine.runAndWait()

    def parseCommand(self):
        self.listener = sr.Recognizer()
        print('Listening...')

        with sr.Microphone() as source:
            self.listener.pause_threshold = 1
            self.listener.adjust_for_ambient_noise(source, duration=1)
            input_speech = self.listener.listen(source)
        try:
            print('Recogizing...')
            query = self.listener.recognize_google(input_speech, language='en_gb')
            print(f'Speech: {query}')
        except Exception as exception:
            return 'None'
        return query
