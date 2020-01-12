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
        MESSAGE["bg"]="red"
#        MESSAGE.pack({"side":"top"})
        MESSAGE.grid(column=0,row=0,columnspan=2,padx=3,pady=3,sticky="NSEW")

        btn_m=Button(sub_w)
        btn_m["text"]="Hi!"
        btn_m.grid(column=0,row=1,padx=2,pady=2,sticky="NSEW")

        btn=Button(sub_w)
        btn["text"]="close"
        btn["command"]=sub_w.quit
        #btn.pack({"side":"bottom"})
        btn.grid(column=1,row=1,padx=2,pady=2,sticky="NSEW")

    def createWidgets(self):

        self.INFO1 = Label(self)
        self.INFO1["text"]="Test"
        self.INFO1["bg"]="blue"
        #self.INFO1.pack({"side":"left"})
        self.INFO1.grid(column=0,row=1,columnspan=2,padx=2,sticky="NSEW")
        self.INFO2 = Label(self)
        self.INFO2["text"]="Message"
        self.INFO2["bg"]="blue"
        #self.INFO2.pack({"side":"left"})
        self.INFO2.grid(column=0,row=2,columnspan=2,padx=2,sticky="NSEW")
        self.INFO2 = Label(self)
        self.INFO2["text"]="Inofometion!"
        self.INFO2["bg"]="blue"
        #self.INFO2.pack({"side":"left"})
        self.INFO2.grid(column=0,row=3,columnspan=2,padx=2,sticky="NSEW")

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        #self.QUIT.pack({"side": "left"})
        self.QUIT.grid(column=0,row=4,padx=2,pady=2,sticky="NSEW")
  
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        #self.hi_there.pack({"side": "left"})
        self.hi_there.grid(column=1,row=4,padx=2,pady=2,sticky="NSEW")

        self.comtent1=Label(self,width=20,height=10,bg="black")
        self.comtent1.grid(column=0,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})

        self.comtent2=Label(self,width=20,height=10,bg="white")
        self.comtent2.grid(column=1,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master,width=300,height=200)
        self.pack(expand=True, fill="both", anchor="center")
        self.createWidgets()

root = Tk()
dispH=root.winfo_screenheight()
dispW=root.winfo_screenwidth()
print("Hight=%s" % dispH)
print("Width=%s" % dispW)
# right 
viewW=int(dispW)-200-5
root.wm_geometry("300x200+%d+0" % (viewW))
app = Application(master=root)
app.mainloop()
root.destroy()
