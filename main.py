import pyttsx3
friend = pyttsx3.init()
text = input("Say something : ")

friend.say(text)
friend.runAndWait()