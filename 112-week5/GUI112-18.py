from tkinter import *
import Pmw
import sys

from click import command

class MenuBarDemo(Frame):
    """Create window with a MenuBar"""

    def __init__(self):
        """Create a MenuBar with items and a Canvas with text"""
        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand=YES, fill=BOTH)
        self.master.title("MenuBar Demo")
        self.master.geometry("500x200")

        self.MyBalloon =Pmw.Balloon(self)
        self.choices = Pmw.MenuBar(self, balloon=self.MyBalloon)
        self.choices.pack(fill=X)

        #Create file menu and items
        self.choices.addmenu("File","Exit")
        """ self.choices.addmenuitem("Format", "command", command = self.closeDemo, label="Exit") """

        #Create Format menu and items
        self.choices.addmenu("Format", "Change font/color")
        self.choices.addmenuitem("Format","command", command = self.closeDemo, label="Exit")
        self.choices.addcascademenu("Format", "Color")
        self.choices.addcascademenu("Format", "Color2")
        self.choices.addmenuitem("Color2","radiobutton",label = "babanın amk",command = self.keep)
        self.choices.addmenuitem("Format", "separator")
        self.choices.addcascademenu("Format", "Font")

        #Add items to Format/Color menu
        colors = ["Black", "Blue", "Red","Green", "Brown", "Pink"]
        self.selectedColor = StringVar() #atadıgımız itemin string degeri neyse ona dönüşüyor
        self.selectedColor.set(colors[0])

        for item in colors:
            self.choices.addmenuitem("Color", "radiobutton", label =item, command =self.changeColor, variable=self.selectedColor)
            self.choices.addmenuitem("Color", "separator")

        #Add items to Format/Font menu
        fonts= ["Times", "Courier", "Helvetica", "Tahoma"]
        self.selectedFont = StringVar()
        self.selectedFont.set(fonts[0])

        for item in fonts:
            self.choices.addmenuitem("Font", "radiobutton", label=item, command = self.changeFont, variable = self.selectedFont)

        #Add a horizontal separator in Font menu
        self.choices.addmenuitem("Font", "separator")

        #Associate checkbutton menu item with BooleanVar object
        self.boldOn = BooleanVar()
        self.choices.addmenuitem("Font", "checkbutton", label ="Bold", command =self.changeFont, variable =self.boldOn)

        #Associate checkbutton menu item with BolleanVar object
        self.italicOn = BooleanVar()
        self.choices.addmenuitem("Font", "checkbutton", label="Italic", command= self.changeFont,variable =self.italicOn)

        #Create Canvas with text
        self.display = Canvas(self, bg="blue")
        self.display.pack(expand=YES, fill=BOTH)
        self.sampleText = self.display.create_text(250, 100, text="Sample Text", font= "Times 48")
    def keep(self):
        print("worked")
    def changeColor(self):
        """Change the color of the texton the Canvas"""
        self.display.itemconfig(self.sampleText, fill = self.selectedColor.get()) #burayı anla

    def changeFont(self):
        """ self.display.itemconfig(self.sampleText, fill = self.selectedColor.get()) """

        #Get selected font and attach size
        newFont = self.selectedFont.get() + " 48"
        
        

        #Determine which checkbutton menu items selected
        if self.boldOn.get():
            newFont += " bold "  
                   

        if self.italicOn.get():
            newFont += " italic "
    
        #Configure sample text to be displayed in selected type
        print(newFont)
        self.display.itemconfig(self.sampleText, font=newFont)

    def closeDemo(self):
        """Exit the Program"""
        sys.exit()

def main():
    MenuBarDemo().mainloop()

huseyin = MenuBarDemo()
huseyin.mainloop()
















