import pyttsx3

engine = pyttsx3.init()  # engine is the object and init() a method for initialization
engine.say("My name is Ashutosh")
engine.runAndWait()