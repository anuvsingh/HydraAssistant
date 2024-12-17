# Hydra Virtual Assistant  

## 🤖 Overview  
Hydra is a voice-activated virtual assistant designed to simplify tasks like:  

- Opening websites (Google, YouTube, X, etc.)  
- Playing music from a custom library  
- Telling jokes and fun facts  
- Responding to user commands with speech recognition and text-to-speech capabilities.  

## 🚀 Features
- **Voice Commands**: Activate Hydra with the wake word "Hydra".
- **Website Access**: Open popular websites like Google, YouTube, and X.
- **Music Playback**: Play songs using predefined links stored in a custom musicLibrary.
- **Entertainment**: Get random jokes or fun facts.
- **Speech Recognition**: Uses Google Speech API for understanding commands.
- **Text-to-Speech**: Hydra responds using text-to-speech (TTS).

## 🛠 Technologies Used
- **Python**  
- **Libraries**:  
  * `speech_recognition` for voice input  
  * `pyttsx3` for text-to-speech conversion  
  * `webbrowser` for website automation  
  * `requests` for fetching jokes from APIs  
- **APIs**:  
  * [JokeAPI](https://jokeapi.dev) for joke fetching  
- **Custom Module**:  
  * `musicLibrary` for managing music links  
