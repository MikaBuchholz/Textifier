from tkinter import *
from imageLogic import ImageLogic
from PIL import Image
import os
import pathlib


class TkInterImg(ImageLogic):
    def __init__(self):
        super().__init__()
        self.correctOutputColor = "Green"
        self.falseOutputColor = "IndianRed3"
        self.buttonColor = "light slate grey"
        self.entryColor = "light blue"
        self.path = os.listdir(pathlib.Path().absolute())
        self.imgVar.set("File")
    
    def mainWindow(self):
        self.root.geometry("250x200")
        self.root.title("ImageText")

        Label(self.root, text = "Textifier", font =("Segoe UI", 15), fg ="IndianRed3").place(x= 90, y = 20)
        Label(self.root, text = "File Name", font =("Segoe UI", 10), fg ="IndianRed3").place(x=20, y = 118)
      
        Checkbutton(self.root, text = "Save", variable = self.saveToFileVar).place(x = 20, y = 157)
        OptionMenu(self.root, self.imgVar, *self.path).place(x = 95, y = 115)
        Button(self.root, text = "Get Text", bg = "black", fg = "white",font =("Segoe UI", 7), command = lambda *args: self.displayText()).place(x = 105, y = 160)

        self.root.mainloop()
    
    def displayText(self):
        root = Tk()
        root.geometry("300x300")

        text = self.saveToFile()
        Label(root, text = text, font =("Segoe UI", 10), fg ="black").place(x=45, y = 100)
        
TkInterImg().mainWindow()