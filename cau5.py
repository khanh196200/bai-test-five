from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH
from tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Checkbutton")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()
        cb = Checkbutton(self,text="Show Title",variable=self.var,command=self.onClick)
        bc=Button(self,text="Button")
        bc.pack()
        bc.place(x=60,y=60)
        cb.select()
        cb.place(x=40,y=40)
    def onClick(self):
        if self.var.get() == True:
            self.master.title("Button")
        else:
            self.master.title("")
            
root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop() 
