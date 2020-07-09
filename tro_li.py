import speech_recognition
import pyttsx3
import cv2
from datetime import date

robot_e = speech_recognition.Recognizer()
robot_m = pyttsx3.init()
robot_r = ""
src = cv2.imread('D:\\Python\\Tro_ly_ao\\hmoobkn.jpg')
while True:
	with speech_recognition.Microphone() as micro:
		print("Robot: I'm listening")
		audio = robot_e.listen(micro)
	print("Robot: .....")
	try:
		you = robot_e.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)
	if you == "how are you":
	 	robot_r = "I'm ok, thank you!"
	elif you == "":
	 	robot_r = "I don't know"
	elif "hello" in you:
		robot_r = "Hi"
	elif "hi" in you:
		robot_r = "Hello !"
	elif "what's your name" in you:
		robot_r = "I'm robot"
	elif "name" in you:
		robot_r = "I'm robot"
	elif "how old" in you:
		robot_r = "I'm one day"
	elif "girl" in you:
		robot_r = "I' am here"
		robot_m.say(robot_r)
		robot_m.runAndWait()
		cv2.imshow('image', src)
		cv2.waitKey(3000)
		cv2.destroyAllWindows()
		robot_r = "may i help you"
	elif "today" in you:
		today = date.today()
		robot_r = today.strftime("%B %d, %Y")
	elif "bye" in you:
		robot_r = "Goodbye"
		robot_m.say(robot_r)
		robot_m.runAndWait()
		print("Robot: " + robot_r)
		break
		exit()
	else:
	 	robot_r = "i don't understand"

	print("Robot: " + robot_r)
	robot_m.say(robot_r)
	robot_m.runAndWait()