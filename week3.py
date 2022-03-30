# radio button yalnız biri seçilebilir.
from curses import BUTTON3_RELEASED
from distutils.command.install import HAS_USER_SITE
from os import WIFCONTINUED
from tkinter import *
from tkinter.messagebox import Message, showinfo
from tkinter import font

from matplotlib.pyplot import fill, text




""" 
class week3_radioButton(Frame):
     def __init__(self) -> None:
         Frame.__init__(self)
         self.pack()
         self.frame1 = Frame()
         self.frame1.pack()
         fontSelections = ["Plain","Bold","Italıc","Bold/Italic"]
         
         
         




         self.chosenFont = StringVar() #anlasılması gerekiyor 

         #baslangıc degeri
         self.chosenFont.set(fontSelections[2])
         self.text = Label(self.frame1,text="initial value",font="bold")
         self.text.pack()
         for style in fontSelections:
              aButton = Radiobutton(self.frame1,text=style,variable=self.chosenFont,value=style,command=self.changeFont)
              print(style)
              aButton.pack(side=LEFT,padx=5,pady=5)
     def changeFont(self):
          myfont = 15
          if self.chosenFont.get()== "Bold": # get sayesinde choseni alıyorsun
               myfont = 25
               
          elif self.chosenFont.get() == "Plain":
              

               myfont = 30

          self.text.config(font=("Italic",myfont)) # config sayesinde yeniliyorsun

huseyin = week3_radioButton()     
mainloop() """


""" class week3_radioButton(Frame):
     def __init__(self) -> None:
         Frame.__init__(self)
         self.pack()
         self.frame1 = Frame()
         self.frame1.pack()

         self.button = Button(self.frame1,height=50,width=50)
         self.button.pack()
         self.button.bind("<ButtonRelease-1>",self.command)
     def command(self,event):
          showinfo("title","content")
     

huseyin = week3_radioButton()
huseyin.mainloop()
 """

""" class week3_radioButton(Frame):
     def __init__(self) -> None:
         Frame.__init__(self)
         self.pack()
         self.frame1 = Frame()
         self.frame1.pack()
         self.textContent = StringVar()
         self.textContent.set("nothing here")

         self.label = Label(self.frame1,textvariable=self.textContent)
         self.label.pack()
         self.label.bind("<Button-1>",self.change)
     def change(self,event):
          print("buraya geliyor")
          if self.textContent != "changed":
               self.textContent.set("changed")
          elif self.textContent == "changed":
               print("worked")
               
          self.label.config(textvariable=self.textContent)

huseyin = week3_radioButton()
mainloop() """

""" 
class week3_radioButton(Frame):
     def __init__(self) -> None:
         Frame.__init__(self)
         self.pack()
         self.frame1 = Frame()
         self.frame1.pack()
         self.textContent = StringVar()
         self.textContent.set("nothing here")
         self.label = Label(self.frame1,textvariable=self.textContent)
         self.label.pack()
         self.master.bind("<KeyRelease>",self.keypressed) #bunu master yapmazsan keyboard giremiyorsın 
     def keypressed(self,event):
          print("geşldi")
          self.textContent.set(event.char) # evet char girilen karakteri gösteriyor 

huseyin = week3_radioButton()
mainloop()

         
 """


 # pack, grid, place
""" root = Tk()
frame = Frame(root)
frame.pack(expand=YES, fill=Y) #expand sayesinde butonları sabitliyoruz örnek:alttaki hep altta kalıyor.fill ile beraber kullanılıca tabi

button = Button(frame,text="yes")
button.pack(side=TOP)
button2 = Button(frame,text="no")
button2.pack(side=BOTTOM, pady=150,ipady=20) #pad css margin, ipad css padding

root.mainloop() """


root = Tk()
frame = Frame(root,bg="green",height=3,width=3)
""" frame.pack(expand=YES,fill=BOTH) """
frame.grid(sticky=W+E+N+S) #sticky sayesinde satbitliyoruz
text1 = Text(frame,height=4,width=15)
text1.grid(sticky=W+E+N+S)
text1.insert(INSERT, "hello world")
#grid ve pack beraber kullanılamıyor 


text2 = Text(frame,height=4,width=15)
text2.grid(rowspan=3,sticky=W+E+N+S)
text2.insert(INSERT, "hello world")
button1 = Button(root,text="button1",width=25)
button1.grid(row=0,column=1,columnspan=5,sticky=W+E+N+S)
button1 = Button(root,text="button1",width=25)
button1.grid(row=1,column=0,columnspan=1,sticky=W+E+N+S)
root.rowconfigure(0,weight=5)
root.columnconfigure(2,weight=5) #bunlar cok önemli fill ve expand gibi kullanılıyor
root.mainloop()

