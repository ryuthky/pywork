#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
#import Tkinter

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"
        sub_w = Toplevel()
        sub_w.overrideredirect(True)
        sub_w.geometry("220x100")

        frame = Frame(sub_w,bg="red")
        frame.pack(expand=True,fill="both")
        #frame.grid(column=0,row=0,sticky="NSEW")
        MESSAGE=Label(frame)
        MESSAGE["text"]="Hi there, everyone"
        MESSAGE["bg"]="red"
#        MESSAGE.pack({"side":"top"})
        MESSAGE.grid(column=0,row=0,columnspan=2,padx=3,pady=3,sticky="NSEW")

        btn_m=Button(frame)
        btn_m["text"]="Hi!"
        btn_m.grid(column=0,row=1,padx=2,pady=2,sticky="NSEW")

        btn_m2=Button(frame)
        btn_m2["text"]="Foget"        
        btn_m2["command"]=sub_w.quit
        btn_m2.grid(column=1,row=1,padx=2,pady=2,sticky="NSEW")

        btn=Button(frame)
        btn["text"]="close"
        btn["command"]=sub_w.quit
        #btn.pack({"side":"bottom"})
        btn.grid(column=2,row=1,padx=2,pady=2,sticky="NSEW")

    def place_pop(self):
        self.p_w = Toplevel()
        self.p_w.geometry("200x200")
        self.p_f=Frame(self.p_w,width=200,height=200)
        self.p_f.pack()

        la=Label(self.p_f,text="Green",bg="green")
        la.place(relx=0.02, rely=0.1, relheight=0.3, relwidth=0.45)

        lb=Label(self.p_f,text="Red",bg="red")
        lb.place(relx=0.47, rely=0.1, relheight=0.2, relwidth=0.51)

        lc=Label(self.p_f,text="Blue",bg="blue")
        lc.place(relx=0.47, rely=0.3, relheight=0.1, relwidth=0.51)

        l1=Label(self.p_f,text="Message1",bg="white")
        l1.place(relx=0.02, rely=0.5, relheight=0.1, relwidth=0.96)
        l2=Label(self.p_f,text="Message2Message2",bg="gray")
        l2.place(relx=0.02, rely=0.6, relheight=0.1, relwidth=0.96)
        l3=Label(self.p_f,text="Message3Message3Message3",bg="white")
        l3.place(relx=0.02, rely=0.7, relheight=0.1, relwidth=0.96)

        b1=Button(self.p_f,text="Hi",command=self.say_hi)
        b1.place(relx=0.03,rely=0.82,relheight=0.1,relwidth=0.44)

        b2=Button(self.p_f,text="QUIT",command=self.p_w.quit)
        b2.place(relx=0.50,rely=0.82,relheight=0.1,relwidth=0.44)

    def createWidgets(self):

        self.INFO1 = Label(self)
        self.INFO1["text"]="Test"
        self.INFO1["bg"]="blue"
        #self.INFO1.pack({"side":"left"})
        self.INFO1.grid(column=0,row=1,columnspan=3,padx=2,sticky="NSEW")
        self.INFO2 = Label(self)
        self.INFO2["text"]="Message"
        self.INFO2["bg"]="blue"
        #self.INFO2.pack({"side":"left"})
        self.INFO2.grid(column=0,row=2,columnspan=3,padx=2,sticky="NSEW")
        self.INFO2 = Label(self)
        self.INFO2["text"]="Inofometion!"
        self.INFO2["bg"]="blue"
        #self.INFO2.pack({"side":"left"})
        self.INFO2.grid(column=0,row=3,columnspan=3,padx=2,sticky="NSEW")

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        #self.QUIT.pack({"side": "left"})
        self.QUIT.grid(column=0,row=4,padx=2,pady=2,sticky="NSEW")

        self.PLACE = Button(self)
        self.PLACE["text"] = "PLACE"
        self.PLACE["fg"]   = "blue"
        self.PLACE["command"] =  self.place_pop
        #self.PLACE.pack({"side": "left"})
        self.PLACE.grid(column=1,row=4,padx=2,pady=2,sticky="NSEW")
 

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        #self.hi_there.pack({"side": "left"})
        self.hi_there.grid(column=2,row=4,padx=2,pady=2,sticky="NSEW")

        self.comtent1=Label(self,width=20,height=10,bg="black")
        self.comtent1.grid(column=0,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})

        self.comtent2=Label(self,width=20,height=10,bg="white")
        self.comtent2.grid(column=1,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})

        self.comtent3=Label(self,width=20,height=10,bg="green")
        self.comtent3.grid(column=2,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master,width=290,height=200)
        self.pack(expand=True, fill="both", anchor="center")
        self.createWidgets()

root = Tk()
dispH=root.winfo_screenheight()
dispW=root.winfo_screenwidth()
print("Hight=%s" % dispH)
print("Width=%s" % dispW)
# right 
viewW=int(dispW)-200-5
root.wm_geometry("450x300+%d+0" % (viewW))
app = Application(master=root)
app.mainloop()
root.destroy()
