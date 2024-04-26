import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()  # Initialize the speech recognizer

    def listen_and_write(self):
        with sr.Microphone() as source:
            print("Speak something...")  # Prompt the user to speak
            
            # Adjust recognizer settings for better recognition
            self.recognizer.energy_threshold = 300  # Adjust energy threshold based on environment
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            
            audio_data = self.recognizer.listen(source)  # Listen to the audio input

            try:
                # Recognize speech with Google Speech Recognition
                text = self.recognizer.recognize_google(audio_data, language="en-US", show_all=False)
                print("You said:", text)  # Print the recognized text
                return text  # Return the recognized text

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")  # Handle unrecognized audio
                return None  # Return None if speech cannot be recognized

if __name__ == "__main__":
    stt = SpeechToText()  # Initialize the SpeechToText object
    stt.listen_and_write()  # Call the listen_and_write method to listen to speech and convert it to text
