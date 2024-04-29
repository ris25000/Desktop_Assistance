from utilities.SpeechToText import SpeechToText
from utilities.TextToSpeech import TextToSpeech
from utilities.Utilities import *
from utilities.gpt_response1 import gpt_response
from g4f.client import Client
from googleapiclient.discovery import build
from utilities.youtube_search import get_youtube_video_link
import webbrowser


def main():
    stt = SpeechToText()
    tts = TextToSpeech()
    client = Client()


    while True:
        try:
            text = stt.listen_and_write()
            if text is None:
                print("Say it again..............")
               
            text = text.lower()
             
        except Exception as e:
            print("Speech not recognized. Please try again.")
            continue  # Continue the loop to lis   ten for speech again

        if "google" in text:
            #tts.tospeech("Opening google.com")
            #  open_website("https://www.google.com")
            # if "on google" in text:
            
            query = text.lower().replace("on google","").replace("google","")
            tts.tospeech("Searching for " + query + " on Google")
            search_on_google(query)
            
        elif "calculator" in text:
            open_calculator()
        
        
        
        
        elif "play" in text or "watch" in text:
            query = text.lower().replace("play", "").replace("playing", "")
            tts.tospeech("Playing" + query + " on YouTube")
            youtube_video_link = get_youtube_video_link(query, "AIzaSyCJrlnTG_mDldHIlgfqDKmprU0atgtV00c")
            if youtube_video_link:
        # Open the video URL in a web browser to play the video
                webbrowser.open(youtube_video_link)
            else:
                tts.tospeech("No video found on YouTube.")

        elif "youtube" in text or "you tube" in text:
            query = text.lower().replace("you tube", "").replace("youtube", "")
            tts.tospeech("Searching for " + query + " on YouTube")
            search_on_youtube(query)


        elif "time" in text:
            current_time_str = str(current_time())
            print("Current time:", current_time_str)
            
            tts.tospeech("The current time is " + current_time_str)
        
        elif "close" in text:
            tts.tospeech(" Thank you for Using  have a  nice   day ")
            break
        elif "bing" in text or "being" in text:
            query = text.lower().replace("on bing","").replace("bing","")
            tts.tospeech("Searching for " + query + " on the browser  Bing")
            search_on_bing(query)
        else:
            tts.tospeech("Let me search for that.")
            gpt_prompt = "What can you tell me about do not include ** in any sentence give only a paragraph " + text
            response = gpt_response(gpt_prompt,client)
            print(response)
            tts.tospeech(response)
            



        


if __name__ == "__main__":
    main()