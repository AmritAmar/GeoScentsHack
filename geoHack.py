import pyautogui
from PIL import Image
import pytesseract
from tkinter import *
from pynput import keyboard
from geopy.geocoders import Nominatim

#Set our OCR Reader to the correct path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Some variables
APP_NAME = "Trying_to_beat_geosense"
KnownLoc = [-34.881368, 19.914208]

#Create new GUI App using tkinter
root = Tk()
root.title("GeoSensEZ")

#GUI Variables
textTopLeftX = IntVar(root, name = "textTopLeftX") 
textTopLeftY = IntVar(root, name = "textTopLeftY") 
textBottomRightX = IntVar(root, name = "textBottomRightX") 
textBottomRightY = IntVar(root, name = "textBottomRightY")
eqLatValue = IntVar(root, name = "eqLatValue")
eqLonValue = IntVar(root, name = "eqLonValue")
ctLatValue = IntVar(root, name = "ctLatValue")
ctLonValue = IntVar(root, name = "ctLonValue")

textValue = StringVar(root, name = "textValue")
latValue = DoubleVar(root, name = "latValue")
lonValue = DoubleVar(root, name = "lonValue")

root.setvar(name = "textTopLeftX", value = 0) 
root.setvar(name = "textTopLeftY", value = 0) 
root.setvar(name = "textBottomRightX", value = 0) 
root.setvar(name = "textBottomRightY", value = 0) 
root.setvar(name = "eqLatValue", value = 0) 
root.setvar(name = "eqLonValue", value = 0) 
root.setvar(name = "ctLatValue", value = 0) 
root.setvar(name = "ctLonValue", value = 0) 

root.setvar(name = "textValue", value = "") 
root.setvar(name = "latValue", value = 0.0) 
root.setvar(name = "lonValue", value = 0.0) 

#New Canvas
canvas1 = Canvas(root, width = 300, height = 700)
canvas1.pack()

#Functions
def getTextCoords():
	# The event listener will be running in this block
	with keyboard.Events() as events:
		for event in events:
			if event.key == keyboard.Key.esc:
				break
			elif event.key == keyboard.Key.space:
				#print('Received event {}'.format(event))
				print(pyautogui.position())
				x, y = pyautogui.position()
				root.setvar(name = "textTopLeftX", value = x) 
				root.setvar(name = "textTopLeftY", value = y) 
				break

def getTextCoords1():
	# The event listener will be running in this block
	with keyboard.Events() as events:
		for event in events:
			if event.key == keyboard.Key.esc:
				break
			elif event.key == keyboard.Key.space:
				#print('Received event {}'.format(event))
				print(pyautogui.position())
				x, y = pyautogui.position()
				root.setvar(name = "textBottomRightX", value = x) 
				root.setvar(name = "textBottomRightY", value = y) 
				break

def getTextCoordsEQ():
	# The event listener will be running in this block
	with keyboard.Events() as events:
		for event in events:
			if event.key == keyboard.Key.esc:
				break
			elif event.key == keyboard.Key.space:
				#print('Received event {}'.format(event))
				print(pyautogui.position())
				x, y = pyautogui.position()
				root.setvar(name = "eqLatValue", value = x) 
				root.setvar(name = "eqLonValue", value = y) 
				break
				
def getTextCoordsCT():
	# The event listener will be running in this block
	with keyboard.Events() as events:
		for event in events:
			if event.key == keyboard.Key.esc:
				break
			elif event.key == keyboard.Key.space:
				#print('Received event {}'.format(event))
				print(pyautogui.position())
				x, y = pyautogui.position()
				root.setvar(name = "ctLatValue", value = x) 
				root.setvar(name = "ctLonValue", value = y) 
				break
 	
def getWord():
	im = pyautogui.screenshot('my_screenshot.png', region=(textTopLeftX.get(), textTopLeftY.get(), textBottomRightX.get() -	textTopLeftX.get(), textBottomRightY.get() - textTopLeftY.get()))
	root.setvar(name = "textValue", value = pytesseract.image_to_string(im).split('(')[0])
	print(textValue.get())
	
def getLatitudeLongitude():
	geolocator = Nominatim(user_agent=APP_NAME)
	location = geolocator.geocode(textValue.get())
	print(location.address)
	print((location.latitude, location.longitude))
	root.setvar(name = "latValue", value = location.latitude)
	root.setvar(name = "lonValue", value = location.longitude)
	
def refreshWordLoc():
	getWord()
	getLatitudeLongitude()
	
def click():
	difX = ctLatValue.get() - eqLatValue.get()
	difY = ctLonValue.get() - eqLonValue.get()
	print(ctLatValue.get(), ctLonValue.get())
	print(eqLatValue.get(), eqLonValue.get())
	print(difX)
	print(difY)
	print(KnownLoc)
	print(latValue.get(), lonValue.get())
	latY = difY / KnownLoc[0]  #amount to move in Y given latitude
	lonX = difX / KnownLoc[1]   #amount to move in X given longitude
	print(latY)
	print(lonX)
	diffPixelsX = lonX * lonValue.get()
	diffPixelsY = latY * latValue.get()
	print(diffPixelsX)
	print(diffPixelsY)
	pyautogui.moveTo(eqLatValue.get() + diffPixelsX, eqLonValue.get() + diffPixelsY)

myButtonT1 = Button(text='Text Top Left', command=getTextCoords, bg='green',fg='white',font= 10)
myButtonT2 = Button(text='Text Bottom Right', command=getTextCoords1, bg='green',fg='white',font= 10)
myButtonEQ = Button(text='Equator', command=getTextCoordsEQ, bg='green',fg='white',font= 10)
myButtonCT = Button(text='Cape-CT', command=getTextCoordsCT, bg='green',fg='white',font= 10)
myButtonW = Button(text='Get Word', command=getWord, bg='green',fg='white',font= 10)
myButtonL = Button(text='Get Location', command=getLatitudeLongitude, bg='green',fg='white',font= 10)
myButtonR = Button(text='Redo W-L', command=refreshWordLoc, bg='green',fg='white',font= 10)
myButtonClick = Button(text='Click', command=click, bg='green',fg='white',font= 10)
MyLabelLoc = Label(root, textvariable=textValue)
MyLabelLat = Label(root, textvariable=latValue)
MyLabelLon = Label(root, textvariable=lonValue)

canvas1.create_window(150, 50, window=myButtonT1)
canvas1.create_window(150, 100, window=myButtonT2)
canvas1.create_window(150, 150, window=myButtonEQ)
canvas1.create_window(150, 200, window=myButtonCT)
canvas1.create_window(150, 250, window=myButtonW)
canvas1.create_window(150, 300, window=myButtonL)
canvas1.create_window(150, 350, window=myButtonR)

canvas1.create_window(150, 400, window=MyLabelLoc)
canvas1.create_window(150, 450, window=MyLabelLat)
canvas1.create_window(150, 500, window=MyLabelLon)

canvas1.create_window(150, 550, window=myButtonClick)

canvas1.pack()

root.mainloop()