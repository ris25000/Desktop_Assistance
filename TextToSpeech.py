import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english+f3')
        self.engine.setProperty('rate', 150)

    def tospeech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

def main():
    tts = TextToSpeech()
    text = "what is your name"
    tts.tospeech(text)

if __name__ == "__main__":
    main()


