from PIL import Image
import pytesseract
from tkinter import *
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = #Path to tesseract.exe

class ImageLogic():
    def __init__(self):
        self.root = Tk()
        self.imgInput = ""
        self.imgVar = StringVar()
        self.saveToFileVar = BooleanVar()
        self.outputText = ""
        self.text = ""
        self.status = None
    
    def getTextfromIMG(self):
        try:
            self.imgInput = str(self.imgVar.get())
            self.text = pytesseract.image_to_string(Image.open(self.imgInput)).strip()

            return [self.text, True]

        except:
            return ["Not a valid File", False]
       
    def saveToFile(self):
        self.status = self.saveToFileVar.get()

        if self.status == True:
            self.text = self.getTextfromIMG()

            if self.text[1]:
                with open("ImgToText.txt", "w") as f:
                    f.write(self.text[0])

                    return self.text[0]

            else:
                return "Text saved in ImgToText.txt"
            
        elif self.status == False:
            self.text = self.getTextfromIMG()

            return self.text 
    


            

