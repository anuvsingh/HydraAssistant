# Importing necessary libraries
import speech_recognition as sr  # For speech recognition
import webbrowser  # For opening websites in a web browser
import pyttsx3  # For text-to-speech conversion
import musicLibrary  # Custom module containing music links
import requests  # type: ignore # For making API requests
import random  # For selecting random jokes/facts

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Predefined jokes and fun facts
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why don’t programmers like nature? It has too many bugs.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How do you comfort a JavaScript bug? You console it.",
    "Why was the developer broke? Because they used up all their cache!",
    "Why did the programmer quit their job? They didn’t get arrays.",
    "What’s a programmer’s favorite hangout place? The Foo Bar.",
    "Why do Java developers wear glasses? Because they can’t C#.",
    "Why did the scarecrow win an award? Because he was outstanding in his field."
]

fun_facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
    "Octopuses have three hearts, and two of them stop beating when they swim.",
    "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
    "Bananas are berries, but strawberries aren’t. Botanically speaking, strawberries are classified as aggregate fruits.",
    "A day on Venus is longer than a year on Venus. It takes Venus about 243 Earth days to rotate once but only 225 Earth days to orbit the Sun.",
    "Sharks existed before trees. Sharks have been around for over 400 million years, while trees appeared around 350 million years ago.",
    "Sloths can hold their breath longer than dolphins. They can slow their heart rate and hold their breath for up to 40 minutes underwater.",
    "Water can boil and freeze at the same time. This phenomenon, known as the 'triple point,' occurs when temperature and pressure are just right.",
    "There’s enough DNA in the human body to stretch from the Sun to Pluto and back—17 times!",
    "Wombat poop is cube-shaped. This helps it stay in place and not roll away, marking their territory effectively."
]

# Function to make the AI assistant speak
def speak(text):
    engine.say(text)  # Convert text to speech
    engine.runAndWait()  # Wait until speaking is done

# Function to fetch a random joke from JokeAPI
def fetch_joke_from_api():
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
        if response.status_code == 200:
            data = response.json()
            if "joke" in data:
                return data["joke"]
        return "Sorry, I couldn't fetch a joke right now!"
    except Exception as e:
        print(f"Error fetching joke: {e}")
        return "Sorry, I couldn't fetch a joke due to a network issue."

# Function to process jokes or fun facts
def tell_joke_or_fact(command):
    if "joke" in command:
        joke = random.choice(jokes)  # Select a random joke from the predefined list
        speak(joke)
        print(joke)
    elif "fun fact" in command:
        fact = random.choice(fun_facts)  # Select a random fun fact
        speak(fact)
        print(fact)

# Function to process commands like opening websites, playing music, or other actions
def processCommand(c):
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open x" in c:
        webbrowser.open("https://x.com")
    elif "play" in c:
        song = c.split("play")[-1].strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    elif "tell me a joke" in c or "fun fact" in c:
        tell_joke_or_fact(c)
    elif "exit" in c:
        speak("Goodbye, my friend!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

# Main function
if __name__ == "__main__":
    speak("Initializing Hydra...")  # Announce Hydra initialization

    while True:
        print("Waiting for wake word 'Hydra'...")
        try:
            # Listen for the wake word
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                wake_word = recognizer.recognize_google(audio).lower()

                if "hydra" in wake_word:
                    speak("Yes, my friend")  # Respond to the wake word
                    print("Hydra is now active...")

                    # Listen for the user's command
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio).lower()

                        # Process the user's command
                        processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")