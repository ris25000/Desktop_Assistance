import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english_in')  # Use a default English voice
        self.engine.setProperty('rate',200 )  # Increase the speaking rate for clearer voice

    def tospeech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

def main():
    tts = TextToSpeech()
    text = "what is your name"
    tts.tospeech(text)

if __name__ == "__main__":
    main()
