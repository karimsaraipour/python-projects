import pyttsx3

#get text from user
text = input('What would you like your computer to say?\n')
#initialize engine and speak
def textToSpeech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

textToSpeech(text)