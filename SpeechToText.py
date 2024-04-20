import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_write(self):
        with sr.Microphone() as source:
            print("Speak something...")
            
            # Adjust recognizer settings for better recognition
            self.recognizer.energy_threshold = 300  # Adjust energy threshold based on environment
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            
            audio_data = self.recognizer.listen(source)

            try:
                # Recognize speech with Google Speech Recognition
                text = self.recognizer.recognize_google(audio_data, language="en-US", show_all=False)
                print("You said:", text)
                return text 

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
                return None

if __name__ == "__main__":
    stt = SpeechToText()
    stt.listen_and_write()
