
import speech_recognition as sr
import webbrowser
import datetime
import subprocess
from SpeechToText import SpeechToText
import webbrowser
import urllib.parse


def search_on_bing(query):
    search_query = urllib.parse.quote_plus(query)
    search_url = "https://www.bing.com/search?q=" + search_query
    webbrowser.open(search_url)
def search_on_youtube(query):
    search_query = urllib.parse.quote_plus(query)
    search_url = "https://www.youtube.com/results?search_query=" + search_query
    webbrowser.open(search_url)

def search_on_google(query):
    search_query = urllib.parse.quote_plus(query)
    search_url = "https://www.google.com/search?q=" + search_query
    webbrowser.open(search_url)


def open_website(url):
    webbrowser.open(url)

def current_time():
    current_time = datetime.datetime.now()
    return current_time

def open_calculator():
    try:
        subprocess.run(['gnome-calculator'])
    except FileNotFoundError:
        print("Calculator application not found.")

def main():
    stt = SpeechToText()
    
    text = stt.listen_and_write()

    if "google" in text:
        open_website("https://www.google.com")
    elif "calculator" in text:
        open_calculator()
    elif "time" in text:
        print("Current time:", current_time())
    else:
        print("Keyword not recognized.")

if __name__ == "__main__":
    main()




