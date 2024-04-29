import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the text-to-speech engine
        self.engine.setProperty('voice', 'english_in')  # Set the default voice to an English accent
        self.engine.setProperty('rate', 200)  # Increase the speaking rate for a clearer voice

    def tospeech(self, text):
        self.engine.say(text)  # Queue the text to be spoken
        self.engine.runAndWait()  # Speak the queued text and wait for completion

def main():
    tts = TextToSpeech()  # Initialize the TextToSpeech object
    text = "what is your name"  # Example text to be spoken
    tts.tospeech(text)  # Call the tospeech method to speak the provided text

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
