import speech_recognition as sr


#prompt user for end behavior
print('Would you like the converted text to be printed in the terminal or be saved in a file"')
endBehavior = input('Choose either "text" OR "file"\n')

#get file from user
if endBehavior == 'file':
    fileLocation = input('Where would you like to store the converted text?\n')

#initialize recognizer
recognizer = sr.Recognizer()

#exceptions might occur while getting user input
try:
    #use microphone as source
    microphone = sr.Microphone()
    with microphone as source:
        #prompt user to begin speaking
        print('Speak!')
        
        #calibrate recognizer,then etrieve audio from recognizer
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        #convert audio to text using Google
        text = recognizer.recognize_google(audio)
        text = text.lower()

#catch exceptions
except sr.RequestError as re:
    print("Results could not be requested from Google Speech Recognition services; {0}".format(re))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand given audio")


if endBehavior == 'file':
    writeFile = open(fileLocation,'w')
    writeFile.write(text)
else:
    print(text)