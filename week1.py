from ctypes import sizeof
from tkinter import *
import webbrowser

from matplotlib.pyplot import fill
from sklearn.linear_model import Ridge


""" 
words meaning----------------
widget:araç

"""


""" import tkinter
tkinter._test() -----test etmek için kullanılır."""

""" 
from turtle import bgcolor
root_ex = Tk()#burda bir window initilaize ediyoruz 
frame_1 = Frame(root_ex) # root_Ex burda master olarak kullanıldı
frame_1.pack() # This geometry manager organizes widgets in blocks before placing them in the parent widget.
red_button = Button(frame_1,text="red", bg="yellow",relief=FLAT,width= 50, height=50)
red_button.pack(side=RIGHT)
greenbutton = Button(frame_1, text="Brown", fg="brown",bg="grey",width=50,height=50)
greenbutton.pack( side = LEFT )
root_ex.mainloop()

-------benim kodlar
 """



""" root_ex = Tk() # Initialize tkinter and create a root window
frame_1 = Frame(root_ex) # root_ex is the master here
frame_1.pack() # This geometry manager organizes widgets in blocks before placing them in the parent widget. 
redbutton = Button(frame_1, text="Red", fg="red", bg="yellow", relief=FLAT) 
redbutton.pack( side = RIGHT)
greenbutton = Button(frame_1, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )
bluebutton = Button(frame_1, text="Blue", fg="blue")
bluebutton.pack( side = RIGHT )
frame_2 = Frame(root_ex)
frame_2.pack()
blackbutton = Button(frame_2, text="Black", fg="black")
blackbutton.pack()
root_ex.mainloop()
hocanın kodlar--------------------
 """

""" 
frame_1 = Frame(Tk())
frame_1.pack()
redbutton = Button(frame_1, text="Red", fg="red", bg="yellow", relief=FLAT) 
redbutton.pack( side = RIGHT)
greenbutton = Button(frame_1, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )
bluebutton = Button(frame_1, text="Blue", fg="blue")
bluebutton.pack( side = RIGHT )
frame_2 = Frame(Tk())
frame_2.pack()
blackbutton = Button(frame_2, text="Black", fg="black") 
blackbutton.pack(side=TOP)
mainloop() """
#frame bir ile frame 2 nin masterleri bir olmadıgı icin farklı iki main window acıldı.




#bu kısımda class ile kullanımı gösterilmiş üzerine calısmalısın.
""" class LabelDemo(Frame):
     def __init__(self):
          Frame.__init__(self)
          self.pack(expand=YES,fill=BOTH)#fill layout icin kullanılır both ise hem x hem de y kordinatı kastedildigini vurgular
          self.master.title("labels")
          

          self.label1 = Label(self,text="label with text")
          self.label1.pack(side=LEFT,)
          self.label2 = Label(self, bitmap="warning")
          self.label2.pack(side=RIGHT)

     def main():
          LabelDemo().mainloop()
LabelDemo.main()
 """



#youtube videosu türü 


# burda butona bir aksiyon verdim
""" root = Tk()
root.geometry("400x400")
class Elder:
     def __init__(self,master) -> None:
         frame = Frame(master)
         frame.pack() # göründüğü üzere pack olmadan oluşturdugun objeyi sayfaya yazdıramıyorsun

         self.mybutton = Button(frame,bg="Green",text="click me",fg="Blue",command=self.printer)
         self.mybutton.pack(side=LEFT)
         master.mainloop()
     def printer(self):
          print("I had clicked")
          webbrowser.open("https://www.youtube.com")
          webbrowser.open("https://www.facebook.com")
          webbrowser.open("https://www.instagram.com")

triedone = Elder(root) """


#border türleri inceleme
borders = {
     "one": FLAT,
     "two":SUNKEN,
     "three":RAISED,
     "four":GROOVE,
     "five":RIDGE

}
window =Tk()
for relief_name,index in borders.items():
     
     frame = Frame(window,relief=SUNKEN)
     print(index)
     frame.pack(side=LEFT)
     label = Button(master=frame,text=relief_name)
     label.pack()
window.mainloop()