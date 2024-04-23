

# Importing necessary modules and functions


from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech
from Utilities import *
from gpt_response1 import gpt_response
from g4f.client import Client
from youtube_search import get_youtube_video_link

# Main program start


def main():
    
    
    # Initializing SpeechToText, TextToSpeech, and GPT-4 client objects
   
   
    stt = SpeechToText()
    tts = TextToSpeech()
    client = Client()

    # Loop to turn on the microphone until the "close" keyword is detected
    
    
    
    while True:
        try:
            # Listening for speech input and converting it to text
           
           
            text = stt.listen_and_write()
            if text is None:
                print("Say it again..............")
            text = text.lower()
        except Exception as e:
            print("Speech not recognized. Please try again.")
            continue  # Continue the loop to listen for speech again

        
        # Checking for specific keywords in the text to perform actions
       
       
        if "on google" in text:
        
            query = text.lower().replace("on google","").replace("google","")
            tts.tospeech("Searching for " + query + " on Google")
            search_on_google(query)
        
        elif "google" in text:
            tts.tospeech("Opening google.com")
            open_website("https://www.google.com")
            
        
       
        elif "calculator" in text:
            # Opening calculator application
            open_calculator()
       
        elif "play" in text:
            # Searching and playing a video on YouTube based on the provided query
            query = text.lower().replace("play", "")
            tts.tospeech("Searching for " + query + " on YouTube.")
            video_url = get_youtube_video_link(query, "AIzaSyB-yNBJbIUVMcWyPq9W4BKXYIoSPr3Mql0")
            if video_url:
                tts.tospeech("Playing " + query + " on YouTube.")
                open_website(video_url)
            else:
                tts.tospeech("No videos found for " + query + " on YouTube.")
        elif "you tube" in text or "youtube" in text:
            
            
            # Searching on YouTube based on the provided query
            
            query = text.lower().replace("you tube", "").replace("youtube", "")
            tts.tospeech("Searching for " + query + " on YouTube")
            search_on_youtube(query)
        
        
        elif "time" in text:
    # Getting and speaking the current time
            current_time_obj = current_time()  # Assuming current_time() returns a datetime object
            current_time_str = current_time_obj.strftime("%H:%M:%S")  # Formatting to only include time
            print("Current time:", current_time_str)
            tts.tospeech("The current time is " + current_time_str)
       
        elif "close" in text:

            # Exiting the program if the "close" keyword is detected
            
            break
        
        elif "bing" in text or "being" in text:
            # Searching on Bing based on the provided query
            query = text.lower().replace("on bing", "").replace("bing", "")
            tts.tospeech("Searching for " + query + " on the Bing browser")
            search_on_bing(query)
        
        else:
          
  # Generating a response using GPT-4 if no specific action is triggered
           
            tts.tospeech("Let me search for that.")
            gpt_prompt = "What can you tell me about do not include ** in any sentence give only important facts or points " + text
            response = gpt_response(gpt_prompt, client)
            print(response)
            tts.tospeech(response)

if __name__ == "__main__":
    main()