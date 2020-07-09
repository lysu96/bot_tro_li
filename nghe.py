import speech_recognition

robot_e = speech_recognition.Recognizer()
with speech_recognition.Microphone() as micro:
	print("Robot: I'm listening")
	audio = robot_e.listen(micro)

try:
	you = robot_e.recognize_google(audio)
except:
	you = ""

print("You: " + you)