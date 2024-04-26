from gtts import gTTS
from pydub import AudioSegment
import pygame
import io

class TextToSpeech:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def tospeech(self, text):
        tts = gTTS(text=text, lang='en')  # Using English language
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)

        audio_data = AudioSegment.from_file(audio_stream, format="mp3")
        pygame.mixer.Sound(audio_data.raw_data).play()

def main():
    tts = TextToSpeech()
    text = "What is your name?"
    tts.tospeech(text)

if __name__ == "__main__":
    main()
