#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"
        sub_w = Toplevel()
        sub_w.overrideredirect(True)
        sub_w.geometry("200x100")
        MESSAGE=Label(sub_w)
        MESSAGE["text"]="Hi there, everyone"
        MESSAGE.pack({"side":"top"})
        btn=Button(sub_w)
        btn["text"]="close"
        btn["command"]=sub_w.quit
        btn.pack({"side":"bottom"})

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
dispH=root.winfo_screenheight()
dispW=root.winfo_screenwidth()
print("Hight=%s" % dispH)
print("Width=%s" % dispW)
# right 
viewW=int(dispW)-200-5
root.wm_geometry("200x200+%d+0" % viewW)
app = Application(master=root)
app.mainloop()
root.destroy()
