from tkinter import *
import Pmw
class CopyMachine(Frame):
     def __init__(self):
          Frame.__init__(self)
          Pmw.initialise() #pmw başlatıldı

          self.pack(expand=YES,fill=BOTH)
          

          self.text1 =Pmw.ScrolledText(self, text_width=25, text_height=12, text_wrap=WORD, hscrollmode= "dynamic", vscrollmode= "dynamic")#burda gerektiğinde scroll edilebilen text field oluşturuyorz.
          self.text1.pack(side=LEFT,expand=YES,fill=BOTH,padx=5,pady=5)

          self.button = Button(self,text="copy",command=self.copyText)
          self.button.pack(side=LEFT,padx=5,pady=5)


          self.text2 =Pmw.ScrolledText(self, text_state=DISABLED, text_width=25, text_height =12, text_wrap= WORD, hscrollmode ="static", vscrollmode="static")
          self.text2.pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)

     def copyText(self):
          self.text2.settext(self.text1.get())
     def main(self):
          self.mainloop()
ali = CopyMachine()
ali.main()