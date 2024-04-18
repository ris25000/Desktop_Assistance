import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_write(self):
        with sr.Microphone() as source:
            print("Speak something...")
            self.recognizer.adjust_for_ambient_noise(source)
            
            audio_data = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio_data)
                print("You said:", text)
                return text 

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
                return None 
