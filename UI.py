from tkinter import *
from tkinter import font
from PIL import Image, ImageDraw, ImageTk
from time import time


def round_rectangle(x1, y1, x2, y2, radius, **kwargs):
    if "alpha" in kwargs:
        fill = root.winfo_rgb(kwargs.pop("fill"))\
                   + (int(kwargs.pop("alpha") * 255),)
        image = Image.new('RGBA',(x2,y2))
        ImageDraw.Draw(image).rounded_rectangle((x1, y1, x2, y2), fill=fill, radius=radius)
        images.append(ImageTk.PhotoImage(image))
        return canvas.create_image(0,0, image=images[-1], anchor="nw")


root = Tk()
canvas = Canvas(root, width = 600, height = 1200)
images=[]      

img0 = PhotoImage(file="Assets/iPhoneBackground.png")      
canvas.create_image(0,0, anchor=NW, image=img0)        
img1 = PhotoImage(file="Assets/iPhone.png")      
canvas.create_image(0,0, anchor=NW, image=img1)
my_rectangle = round_rectangle(50, 1020, 550, 1140, 20, fill="white", alpha=0.35)

#List of dictionaries that each contain info on an app or folder
items = [
    {
    "name": "Camera", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 0,
    "y-order": 0,
    "categories": ["Built-in"]
    },
    {
    "name": "Messages", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 1,
    "y-order": 0,
    "categories": ["Built-in"]
    },
    {
    "name": "Settings", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 2,
    "y-order": 0,
    "categories": ["Built-in"]
    },
    {
    "name": "Clash Of Clans", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 3,
    "y-order": 0,
    "categories": ["Games"]
    },
    {
    "name": "Candy Crush", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 0,
    "y-order": 1,
    "categories": ["Games"]
    },
    {
    "name": "Clash Of Clans", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 1,
    "y-order": 1,
    "categories": ["Games"]
    },
    {
    "name": "Tinder", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 2,
    "y-order": 1,
    "categories": ["Dating"]
    },
    {
    "name": "OkCupid", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 3,
    "y-order": 1,
    "categories": ["Dating"]
    },
    {
    "name": "SomeFolder", 
    "type": "folder",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "n/a",
    "x-order": 0,
    "y-order": 2,
    "categories": "n/a"
    },
    {
    "name": "SomeApp1", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "SomeFolder", 
    "x-order": 0,
    "y-order": 0,
    "categories": ["Test"]
    },
    {
    "name": "SomeApp2", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "SomeFolder", 
    "x-order": 1,
    "y-order": 0,
    "categories": ["Test"]
    },
    {
    "name": "SomeApp3", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "SomeFolder", 
    "x-order": 2,
    "y-order": 0,
    "categories": ["Test"]
    },
    {
    "name": "SomeApp4", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "SomeFolder", 
    "x-order": 0,
    "y-order": 1,
    "categories": ["Test"]
    },
]

def rightClickCallback(event):
    print("Hi")

inFolder = False
def leftClickCallback(event):
    global inFolder

    if inFolder:
        inFolder = False
    else:
        inFolder = True
        

def getAppImageCoordinates(item):
    if item["folder"] == "" or item["folder"] == "n/a":
        return (75 + item["x-order"] * 120, 150 + item["y-order"] * 150)
    else:
        return (125 + item["x-order"] * 120, 400 + item["y-order"] * 150)

def getAppNameCoodinates(item):
    if item["folder"] == "" or item["folder"] == "n/a":
        return (125 + item["x-order"] * 120, 265 + item["y-order"] * 150)
    else:
        return (175 + item["x-order"] * 120, 520 + item["y-order"] * 150)


def renderBackground():
    canvas.create_image(0,0, anchor=NW, image=img0)              
    canvas.create_image(0,0, anchor=NW, image=img1)
    my_rectangle = round_rectangle(50, 1020, 550, 1140, 20, fill="white", alpha=0.35)
    canvas.pack()

def renderHomeScreen():
    for item in items:
        if item["folder"] == "" or item["folder"] == "n/a":
            imageCoordinates = getAppImageCoordinates(item)
            nameCoordinates = getAppNameCoodinates(item)
            canvas.create_text(nameCoordinates[0], nameCoordinates[1], text=item["name"])
            canvas.create_image(imageCoordinates[0], imageCoordinates[1], anchor=NW, image=item["image"])
    canvas.pack()

def renderFolder(folderName):
    canvas.create_rectangle(100,350, 500, 850, fill='gray')
    canvas.create_text(300, 300, text=folderName, font=font.Font(family='Helvetica', size=32))
    for item in items:
        if item["folder"] == folderName:
            imageCoordinates = getAppImageCoordinates(item)
            nameCoordinates = getAppNameCoodinates(item)
            canvas.create_text(nameCoordinates[0], nameCoordinates[1], text=item["name"])
            canvas.create_image(imageCoordinates[0], imageCoordinates[1], anchor=NW, image=item["image"])
    canvas.pack()



canvas.bind("<Button-1>", leftClickCallback)
canvas.bind("<Button-3>", rightClickCallback)
while True:
    renderBackground()
    renderHomeScreen()
    if inFolder:
        renderFolder("SomeFolder")
    root.update_idletasks()
    root.update()