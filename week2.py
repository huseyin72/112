
from tkinter import *
from tkinter.messagebox import *

from click import command
""" def hello(event):  #event handler kullandıgımzda fonksiyon içine bunu bu şekilde parametre olarak bildirmeliyiz.
     print("single click button1")
def quit(event):
     print("double click")
     import sys;sys.exit()#programı sonlandırır
widget = Button(None,text="mause clicked")
widget.pack()
widget.bind("<Button-1>",hello)#sol mause tuşuna bir kere basıldıgınında calısır.
widget.bind("<Double-1>",quit)#sol mause tuşuna iki kere basıldıgınında calısır.

widget.mainloop() """



#motion eventi

""" def hello(event):  #event handler kullandıgımzda fonksiyon içine bunu bu şekilde parametre olarak bildirmeliyiz.
     print("(%s %s)" %(event.x,event.y))
def quit(event):
     print("double click")
     import sys;sys.exit()#programı sonlandırır
widget = Button(None,text="mause clicked",height=50,width=50)
widget.pack()
widget.bind("<Motion>",hello)#mause widge üzerinde hareket ettigi sürece calısır.
widget.bind("<Double-1>",quit)#sol mause tuşuna iki kere basıldıgınında calısır.

widget.mainloop()  """




#enter ve leave kullanımı.
""" def enter(event):
     print("enter worked")
def leave(event):
     print("leave worked")
master = Tk()
message = Message(master,text="merhava ",bg="blue")
message.bind("<Enter>",enter)
message.bind("<Leave>",leave)

message.pack()
master.mainloop() """


#entry kullanımı 
""" master = Tk()
frame1 = Frame(master)
frame1.pack()
l1 = Label(frame1,text="entry one")
l1.pack(side=LEFT)
e1 = Entry(frame1,)
e1.pack(side=LEFT)
master.mainloop() """

#return eventini görecez burda
""" class Demo(Frame):
     def __init__(self):
          Frame.__init__(self)
          self.pack(expand=YES,fill=BOTH)
          self.frame1 = Frame()
          self.frame1.pack(pady=5)


          self.text1 = Entry(self.frame1,name="text1")
          self.text1.bind("<Return>",self.showContent)
          self.text1.pack(side=LEFT,padx=5)


          self.text2 = Entry(self.frame1,name="text2")
          self.text2.insert(INSERT,"enter text here")
          self.text2.bind("<Return>",self.showContent)
          self.text2.pack(side=LEFT,padx=5)





          self.frame2 = Frame()
          self.frame2.pack(pady=5)


          self.text3 = Entry(self.frame2,name="text3")
          self.text3.insert(INSERT,"uneditable text field")
          self.text3.config(state=DISABLED)
          self.text3.bind("<Return>",self.showContent)
          self.text3.pack(side=LEFT,padx=5)


          self.text4 = Entry(self.frame2,name="text2",show="*")
          self.text4.insert(INSERT,"any text should be hidden")
          self.text4.bind("<Return>",self.showContent)
          self.text4.pack(side=LEFT,padx=5)

     def showContent(self,event):
          theName = event.widget.winfo_name()
          theContents = event.widget.get()
          showinfo("message",theName + theContents)

     def main(self):
          self.mainloop()



huseyin = Demo()
huseyin.main()




 """

 #check button yapılışı

"""class Checkbuttonn(Frame):
     def __init__(self):
          Frame.__init__(self)
          self.pack(expand=YES,fill=BOTH)
          self.frame1 = Frame(self)
          self.frame1.pack()

          self.text1 = Entry(self.frame1,font="arial 10")
          self.text1.insert(INSERT,"selamm")
          
          self.text1.pack()

          self.frame2 = Frame(self)
          self.frame2.pack()

          self.booleanOn = BooleanVar()
          self.booleanOn2 = BooleanVar()
          self.button1 = Checkbutton(self.frame1,text="bold",variable=self.booleanOn,command=self.bolder)
          self.button2 = Checkbutton(self.frame1,text="italic",variable=self.booleanOn2,command=self.bolder)

          self.button1.pack(side=LEFT)
          self.button2.pack(side=LEFT)

     def bolder(self):
          desiredFont = "arial 10"
          if self.booleanOn.get():
               desiredFont += " bold"
          if self.booleanOn2.get():
               desiredFont += " italic"
          self.text1.config (font=desiredFont)
     def main(self):
          self.mainloop()

huseyin = Checkbuttonn()
huseyin.main() """
          


