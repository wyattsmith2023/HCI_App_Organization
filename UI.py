from tkinter import *
from PIL import Image, ImageDraw, ImageTk


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
# Apps
#Row 1
app0 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(125,265, text="Clash Of Clans")
canvas.create_image(75,150, anchor=NW, image=app0)
app1 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(242,265, text="Clash Of Clans")
canvas.create_image(192,150, anchor=NW, image=app1)
app2 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(358,265, text="Clash Of Clans")
canvas.create_image(308,150, anchor=NW, image=app2)
app3 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(478,265, text="Clash Of Clans")
canvas.create_image(425,150, anchor=NW, image=app3)
#Row 2
app4 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(125,415, text="Clash Of Clans")
canvas.create_image(75,300, anchor=NW, image=app4)
app5 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(242,415, text="Clash Of Clans")
canvas.create_image(192,300, anchor=NW, image=app5)
app6 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(358,415, text="Clash Of Clans")
canvas.create_image(308,300, anchor=NW, image=app6)
app7 = PhotoImage(file="Assets/ClashOfClans.png")
canvas.create_text(478,415, text="Clash Of Clans")
canvas.create_image(425,300, anchor=NW, image=app7)
canvas.pack()
mainloop()