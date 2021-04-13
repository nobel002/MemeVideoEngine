import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id) 
engine.say("Hello how are you? I'm fine")
engine.runAndWait()