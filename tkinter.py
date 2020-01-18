#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
#import Tkinter

class Application(Frame,object):
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
    def main_pop_hide(self):
        self.master.wm_withdraw()

    def main_pop_raise(self):
        self.p_w.destroy()
        self.comtent1["text"]=self.entry_text1.get()
        self.comtent2["text"]=self.entry_text2.get()
        self.comtent3["text"]=self.entry_text3.get()
        self.master.wm_deiconify()
        
    def character_limit(self,entrychk):
        if len(entrychk.get()) > 0:
            entrychk.set(entrychk.get()[:5])
    def entrychk1(self,*args):
        self.character_limit(self.entry_text1)
    def entrychk2(self,*args):
        self.character_limit(self.entry_text2)
    def entrychk3(self,*args):
        self.character_limit(self.entry_text3)
    def entryclear(self):
        self.entry_text1.set("")
        self.entry_text2.set("")
        self.entry_text3.set("")
    def place_pop(self):
        self.main_pop_hide()
        self.p_w = Toplevel(self)
        self.p_w.geometry("200x300")
        self.p_f=Frame(self.p_w,width=200,height=400)
        self.p_f.pack()

        la=Label(self.p_f,text="Green",bg="green")
        la.place(relx=0.02, rely=0.1, relheight=0.3, relwidth=0.45)

        lb=Label(self.p_f,text="Red",bg="purple",fg="white")
        lb.place(relx=0.47, rely=0.1, relheight=0.2, relwidth=0.51)

        lc=Label(self.p_f,text="Blue",bg="blue")
        lc.place(relx=0.47, rely=0.3, relheight=0.1, relwidth=0.51)

        l1=Label(self.p_f,text="Message1",bg="white")
        l1.place(relx=0.02, rely=0.4, relheight=0.05, relwidth=0.96)
        l2=Label(self.p_f,text="Message2Message2",bg="gray")
        l2.place(relx=0.02, rely=0.45, relheight=0.05, relwidth=0.96)
        l3=Label(self.p_f,text="Message3Message3Message3",bg="white")
        l3.place(relx=0.02, rely=0.50, relheight=0.05, relwidth=0.96)


        e1=Entry(self.p_f,textvariable = self.entry_text1)
        e1.place(relx=0.02, rely=0.55, relheight=0.1, relwidth=0.96)

        e2=Entry(self.p_f,textvariable = self.entry_text2)
        e2.place(relx=0.02, rely=0.65, relheight=0.1, relwidth=0.96)

        e3=Entry(self.p_f,textvariable = self.entry_text3)
        e3.place(relx=0.02, rely=0.75, relheight=0.1, relwidth=0.96)

        b1=Button(self.p_f,text="INPUT",command=self.main_pop_raise)
        b1.place(relx=0.05,rely=0.9,relheight=0.08,relwidth=0.25)

        b2=Button(self.p_f,text="CANCEL",command=self.entryclear)
        b2.place(relx=0.40,rely=0.9,relheight=0.08,relwidth=0.25)

        b3=Button(self.p_f,text="QUIT",command=self.quit)
        b3.place(relx=0.70,rely=0.9,relheight=0.08,relwidth=0.25)

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

        self.comtent1=Label(self,width=20,height=10,bg="black",fg="white")
        self.comtent1.grid(column=0,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})

        self.comtent2=Label(self,width=20,height=10,bg="white")
        self.comtent2.grid(column=1,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})

        self.comtent3=Label(self,width=20,height=10,bg="green")
        self.comtent3.grid(column=2,row=5,padx=2,sticky="E")
        #self.comtents.pack({"side": "left"})


    def __init__(self, master=None):
        #Frame.__init__(self, master,width=290,height=200)
        super(Application,self).__init__(master)#,width=290,height=200)
        dispH=self.master.winfo_screenheight()
        dispW=self.master.winfo_screenwidth()
        print("Hight=%s" % dispH)
        print("Width=%s" % dispW)
        # right 
        viewX=int(dispW)-200-5
        self.master.wm_geometry("450x300+%d+0" % (viewX))
        self.pack(expand=True, fill="both", anchor="center")
        self.createWidgets()
        self.entry_text1= StringVar()
        self.entry_text2= StringVar()
        self.entry_text3= StringVar()
        self.entry_text1.trace("w",self.entrychk1)
        self.entry_text2.trace("w",self.entrychk2)
        self.entry_text3.trace("w",self.entrychk3)

"""main"""
def main():
    root = Tk()
    #root.wm_geometry("450x300+%d+0" % (viewW))
    root.title("MainFrame")
    app = Application(master=root)
    app.mainloop()
    root.destroy()

if __name__ == "__main__":
    main()
