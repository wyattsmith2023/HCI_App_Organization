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
    "image": PhotoImage(file="Assets/Camera.png"), 
    "folder": "", 
    "x-order": 0,
    "y-order": 0,
    "category": "Built-in"
    },
    {
    "name": "Messages", 
    "type": "app",
    "image": PhotoImage(file="Assets/Messages.png"), 
    "folder": "", 
    "x-order": 1,
    "y-order": 0,
    "category": "Built-in"
    },
    {
    "name": "Settings", 
    "type": "app",
    "image": PhotoImage(file="Assets/Settings.png"), 
    "folder": "", 
    "x-order": 2,
    "y-order": 0,
    "category": "Built-in"
    },
    {
    "name": "Clash Of Clans", 
    "type": "app",
    "image": PhotoImage(file="Assets/ClashOfClans.png"), 
    "folder": "", 
    "x-order": 3,
    "y-order": 0,
    "category": "Games"
    },
    {
    "name": "Candy Crush", 
    "type": "app",
    "image": PhotoImage(file="Assets/CandyCrush.png"), 
    "folder": "", 
    "x-order": 0,
    "y-order": 1,
    "category": "Games"
    },
    {
    "name": "Dragonvale", 
    "type": "app",
    "image": PhotoImage(file="Assets/Dragonvale.png"), 
    "folder": "", 
    "x-order": 1,
    "y-order": 1,
    "category": "Games"
    },
    {
    "name": "Tinder", 
    "type": "app",
    "image": PhotoImage(file="Assets/Tinder.png"), 
    "folder": "", 
    "x-order": 2,
    "y-order": 1,
    "category": "Dating"
    },
    {
    "name": "OkCupid", 
    "type": "app",
    "image": PhotoImage(file="Assets/OkCupid.png"), 
    "folder": "", 
    "x-order": 3,
    "y-order": 1,
    "category": "Dating"
    },
    {
    "name": "SomeFolder", 
    "type": "folder",
    "image": PhotoImage(file="Assets/Folder.png"), 
    "folder": "n/a",
    "x-order": 0,
    "y-order": 2,
    "categories": "n/a"
    },
    {
    "name": "SomeApp1", 
    "type": "app",
    "image": PhotoImage(file="Assets/AppStore.png"), 
    "folder": "SomeFolder", 
    "x-order": 0,
    "y-order": 0,
    "category": "Test"
    },
    {
    "name": "SomeApp2", 
    "type": "app",
    "image": PhotoImage(file="Assets/AppStore.png"), 
    "folder": "SomeFolder", 
    "x-order": 1,
    "y-order": 0,
    "category": "Test"
    },
    {
    "name": "SomeApp3", 
    "type": "app",
    "image": PhotoImage(file="Assets/AppStore.png"), 
    "folder": "SomeFolder", 
    "x-order": 2,
    "y-order": 0,
    "category": "Test"
    },
    {
    "name": "SomeApp4", 
    "type": "app",
    "image": PhotoImage(file="Assets/AppStore.png"), 
    "folder": "SomeFolder", 
    "x-order": 0,
    "y-order": 1,
    "category": "Test"
    },
]

#Planning on having right click activate our solution where it automatically organizes the apps
def rightClickCallback(event):
    #Remove all existing folders and references to folders
    i = 0
    while i < len(items):
        if items[i]["type"] == "folder":
            items.pop(i)
            continue
        if items[i]["folder"] != "n/a":
            #If an app was already on the home screen
            if items[i]["folder"] == "":
                i += 1
                continue

            
            items[i]["folder"] = ""
            #Find new positions for any apps that were in folders
            newPosition = (0, 0)
            for y in range(6):
                for x in range(4):
                    newPosition = (x, y)
                    for positionCheckItem in items:
                        if positionCheckItem["folder"] == "" and positionCheckItem["x-order"] == x and positionCheckItem["y-order"] == y:
                            newPosition = (0, 0)
                            break
                    if newPosition != (0, 0):
                        break
                if newPosition != (0, 0):
                    break
            items[i]["x-order"] = newPosition[0]
            items[i]["y-order"] = newPosition[1]
        i += 1
    
    #Categorize apps
    categories = {}
    for app in items:
        if app["category"] not in categories:
            categories[app["category"]] = [app["name"]]
        else:
            categories[app["category"]].append(app["name"])

    categoryIndex = 0
    #Create new folders for each category
    for category in categories:
        items.append({
            "name": category, 
            "type": "folder",
            "image": PhotoImage(file="Assets/Folder.png"), 
            "folder": "n/a", 
            "x-order": categoryIndex % 4,
            "y-order": categoryIndex // 4,
            "category": "n/a"
        })
        categoryIndex += 1

    #Re-folder and reposition apps
    for app in items:
        if app["type"] != "folder":
            app["folder"] = app["category"]
            app["x-order"] = categories[app["category"]].index(app["name"]) % 3
            app["y-order"] = categories[app["category"]].index(app["name"]) // 3
        

inFolder = False
currentFolder = ""
def leftClickCallback(event):
    global inFolder
    global currentFolder

    if inFolder:
        #Leave folder if there's a click outside the folder bounds
        if event.x < 100 or event.x > 500 or event.y < 350 or event.y > 850:
            inFolder = False
    else:
        #Check to see if any folders are being clicked on
        for item in items:
            if item["type"] == "folder":
                imageCoordinates = getItemImageCoordinates(item)
                if event.x > imageCoordinates[0] and event.x < imageCoordinates[0] + 100 and event.y > imageCoordinates[1] and event.y < imageCoordinates[1] + 100:
                    currentFolder = item["name"]
                    inFolder = True
                    break

        
#Gets whatever coordinates an item's image should be at
def getItemImageCoordinates(item):
    #If the item isn't in a folder or the item is a folder itself...
    if item["folder"] == "" or item["folder"] == "n/a":
        return (75 + item["x-order"] * 120, 150 + item["y-order"] * 150)
    else:
        return (125 + item["x-order"] * 120, 400 + item["y-order"] * 150)

#Gets whatever coordinates an item's name should be at
def getItemNameCoodinates(item):
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
            imageCoordinates = getItemImageCoordinates(item)
            nameCoordinates = getItemNameCoodinates(item)
            canvas.create_text(nameCoordinates[0], nameCoordinates[1], text=item["name"])
            canvas.create_image(imageCoordinates[0], imageCoordinates[1], anchor=NW, image=item["image"])
    canvas.pack()

def renderFolder(folderName):
    canvas.create_rectangle(100, 350, 500, 850, fill='gray')
    canvas.create_text(300, 300, text=folderName, font=font.Font(family='Helvetica', size=32))
    for item in items:
        if item["folder"] == folderName:
            imageCoordinates = getItemImageCoordinates(item)
            nameCoordinates = getItemNameCoodinates(item)
            canvas.create_text(nameCoordinates[0], nameCoordinates[1], text=item["name"])
            canvas.create_image(imageCoordinates[0], imageCoordinates[1], anchor=NW, image=item["image"])
    canvas.pack()


#Bind left and right click to callback functions
canvas.bind("<Button-1>", leftClickCallback)
canvas.bind("<Button-2>", rightClickCallback)
while True:
    renderBackground()
    renderHomeScreen()
    if inFolder:
        renderFolder(currentFolder)
    root.update_idletasks()
    root.update()