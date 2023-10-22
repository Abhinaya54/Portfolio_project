#pip install pyttsx3
import pyttsx3 as p
# Initialize the text-to-speech engine
text_speech = p.init()
# Prompt the user for input
answer = input("What you want to convert:")
# Make the text-to-speech engine say the user's input
text_speech.say(answer)
# Wait for the speech to finish before continuing
text_speech.runAndWait()
# Stop the text-to-speech engine
text_speech.stop()  