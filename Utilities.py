
import speech_recognition as sr
import webbrowser
import datetime
import subprocess
from SpeechToText import SpeechToText  # Assuming SpeechToText class is defined in 'SpeechToText' module
import urllib.parse

# Function to search a query on Bing
def search_on_bing(query):
    search_query = urllib.parse.quote_plus(query)  # Encode query for URL
    search_url = "https://www.bing.com/search?q=" + search_query
    webbrowser.open(search_url)  # Open Bing search results in default web browser

# Function to search a query on YouTube
def search_on_youtube(query):
    search_query = urllib.parse.quote_plus(query)  # Encode query for URL
    search_url = "https://www.youtube.com/results?search_query=" + search_query
    webbrowser.open(search_url)  # Open YouTube search results in default web browser

# Function to search a query on Google
def search_on_google(query):
    search_query = urllib.parse.quote_plus(query)  # Encode query for URL
    search_url = "https://www.google.com/search?q=" + search_query
    webbrowser.open(search_url)  # Open Google search results in default web browser

# Function to open a specified website
def open_website(url):
    webbrowser.open(url)  # Open specified URL in default web browser

# Function to get current time
def current_time():
    current_time = datetime.datetime.now()  # Get current datetime
    return current_time

# Function to open calculator application
def open_calculator():
    try:
        subprocess.run(['gnome-calculator'])  # Open calculator application using subprocess
    except FileNotFoundError:
        print("Calculator application not found.")  # Handle FileNotFoundError if calculator application is not found

# Main function to execute commands based on speech input
def main():
    stt = SpeechToText()  # Initialize SpeechToText object for speech recognition
    
    text = stt.listen_and_write()  # Get speech input and convert it to text using SpeechToText

    if "google" in text:
        open_website("https://www.google.com")  # Open Google homepage if 'google' is mentioned in the input
    elif "calculator" in text:
        open_calculator()  # Open calculator application if 'calculator' is mentioned in the input
    elif "time" in text:
        print("Current time:", current_time())  # Print current time if 'time' is mentioned in the input
    else:
        print("Keyword not recognized.")  # Print message if none of the recognized keywords are mentioned in the input

if __name__ == "__main__":
    main()  # Execute main function if the script is executed directly




