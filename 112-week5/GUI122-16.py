from tkinter import *
import Pmw

class ImageSelection(Frame):
    """List of available images and an area to display them"""

    def __init__(self,images):
        """Create list of Photoimages and Label to display them"""
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Select an image")
        Pmw.initialise()

        self.photos = []

        #Add Photoimages objects to list photos
        for item in images:
            self.photos.append(PhotoImage(file = item))

            #Create scrolled list box with vertical scrollbar
            self.listBox = Pmw.ScrolledListBox(self, items=images, listbox_height=3, vscrollmode="static", listbox_selectmode="SINGLE", selectioncommand=self.switchImage)
            self.listBox.pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)
            self.display =Label(self, image=self.photos[0])
            self.display.pack(padx=5, pady=5)

    def switchImage(self):
        """Change image in Label to current selection"""

        #Get tuple containing index of selected list item
        chosenPicture = self.listBox.curselection() #(0,) or (1,)

        #Configure label to display selected image
        if chosenPicture:
            choice =int(chosenPicture[0]) # int here is optional
            self.display.config(image=self.photos[choice])

    def main():
        images = ["logo.png","logo.png"]
        ImageSelection(images).mainloop()

ImageSelection.main()


