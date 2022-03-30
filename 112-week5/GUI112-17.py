from tkinter import *
import Pmw

class CopyTextWindow(Frame):
    """Demonstrate ScrolledText"""

    def __init__(self):
        """Create two ScrolledText and Button"""

        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand=YES, fill=BOTH)
        self.master.title("ScorlledText Demo")

        #Create scrolled text box with word wrap enabled
        self.text1 =Pmw.ScrolledText(self, text_width=25, text_height=12, text_wrap=WORD, hscrollmode= "dynamic", vscrollmode= "dynamic")
        self.text1.pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)

        self.copyButton = Button(self, text="Copy", command=self.copyText)
        self.copyButton.pack(side=LEFT, padx=5, pady=5)

        #Create uneditable scrolled text box
        self.text2 =Pmw.ScrolledText(self, text_state=DISABLED, text_width=25, text_height =12, text_wrap= WORD, hscrollmode ="static", vscrollmode="static")
        self.text2.pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)

    def copyText(self):
        """Set the text in the second ScrolledText"""
        self.text2.settext(self.text1.get())

    def main():
        CopyTextWindow().mainloop()

CopyTextWindow().mainloop()