#! /usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
import os
import tkinter as tk
import logging
import logging.config
import datetime

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('customer')

class mycalender(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        tk.Frame.__init__(self,master,cnf,**kw)
        now = datetime.datetime.now()
        self.year = now.year
        self.month = now.month
        self.date = now
        logger.info("%s/%s/%s",now.year,now.month,now.day)
        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)
        self.previous_month = tk.Label(frame_top, text = "<", font = ("",14))
        self.previous_month.pack(side = "left", padx = 10)
        self.current_year = tk.Label(frame_top, text = self.year, font = ("",18))
        self.current_year.pack(side = "left")
        self.current_month = tk.Label(frame_top, text = self.month, font = ("",18))
        self.current_month.pack(side = "left")
        self.next_month = tk.Label(frame_top, text = ">", font = ("",14))
        self.next_month.pack(side = "left", padx = 10)
        self.previous_month.bind("<1>",self.change_month)
        self.next_month.bind("<1>",self.change_month)
        # frame_week部分の作成
        frame_week = tk.Frame(self)
        frame_week.pack()
        button_mon = d_button(frame_week, text = "Mon")
        button_mon.grid(column=0,row=0)
        button_tue = d_button(frame_week, text = "Tue")
        button_tue.grid(column=1,row=0)
        button_wed = d_button(frame_week, text = "Wed")
        button_wed.grid(column=2,row=0)
        button_thu = d_button(frame_week, text = "Thu")
        button_thu.grid(column=3,row=0)
        button_fri = d_button(frame_week, text = "Fri")
        button_fri.grid(column=4,row=0)
        button_sta = d_button(frame_week, text = "Sat", fg = "blue")
        button_sta.grid(column=5,row=0)
        button_san = d_button(frame_week, text = "San", fg = "red")
        button_san.grid(column=6,row=0)

        # frame_calendar部分の作成
        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()

        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year,self.month)
        self.current_day()
 
    def create_calendar(self,year,month):
        # calendarモジュールのインスタンスを作成    
        import calendar
        cal = calendar.Calendar()
        # 指定した年月のカレンダーをリストで返す
        days = cal.monthdayscalendar(year,month)

    # ボタンがある場合には削除する（初期化）
        try:
            for key,item in self.day.items():
                item.destroy()
        except:
            pass
        # 日付ボタンを格納する変数をdict型で作成
        self.day = {}
        # for文を用いて、日付ボタンを生成
        j=1
        for i in range(0,42):
            c = i - (7 * int(i/7))
            r = int(i/7)
            try:
                # 日付が0でなかったら、ボタン作成
                if days[r][c] != 0:
                    self.day[j] = d_button(self.frame_calendar,text = days[r][c])
                    self.day[j].grid(column=c,row=r)
                    j+=1
            except:
                break
        self.etonum(year)

    # def select_day(self,event):
    #     day = event.widget["text"]
    #     logger.debug("%s日",day)
    #     if event.widget["bg"] == "SystemButtonFace":
    #         event.widget["bg"] = "red"
    #     # 赤色になっていたら、元に戻す。
    #     else:
    #         event.widget["bg"] = "SystemButtonFace"
    def current_day(self):
        logger.debug("%s日",self.date.day)
        dw=self.day[self.date.day]
        if  dw != None:
            dw["bg"]="yellow"
        

    def change_month(self,event):
        if(event.widget["text"] == "<"):
            self.month -=1
        else:
            self.month +=1
    # 月が0、13になったときの処理
        if self.month == 0:
            self.year -= 1
            self.month = 12
        elif self.month == 13:
            self.year +=1
            self.month =1
        logger.debug("%s:%s",self.year,self.month)
        # frame_topにある年と月のラベルを変更する
        self.current_year["text"] = self.year
        self.current_month["text"] = self.month
        # 
        self.create_calendar(self.year,self.month)

    def etonum(self,year):
        kan={0:"甲",1:"乙",2:"丙",3:"丁",4:"戊",5:"己",6:"庚",7:"辛",8:"壬",9:"癸"}
        shi={0:"子",1:"丑",2:"寅",3:"卯",4:"辰",5:"巳",6:"午",7:"未",8:"申",9:"酉",10:"戌",11:"亥"}
        yval = year
        kval = (yval-4)%10
        sval = (yval-4)%12
        kanval = kan[kval]
        shival = shi[sval]
        print("%s:%s%s",yval,kanval,shival)
    # http://www.asahi-net.or.jp/~jc1y-ishr/koyomi_keisan/KoyomiKeisan7.html

# デフォルトのボタンクラス
class d_button(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",14),height=2, width=4, relief="flat")
        self.bind("<1>",self.bgcolorchg)
    def bgcolorchg(self,event):
        if event.widget["bg"] == "SystemButtonFace":
            event.widget["bg"] = "red"
        # 赤色になっていたら、元に戻す。
        else:
            event.widget["bg"] = "SystemButtonFace"
        

def main():
    print("Hello Py:",os.path.basename(__file__))
    logger.info("Hello Py")
    root = tk.Tk()
    root.title("Calender")
    mycal=mycalender(root)
    mycal.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
