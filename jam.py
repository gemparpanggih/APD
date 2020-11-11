from tkinter import *
import time
from math import cos,sin,pi

class MyApp():
    def __init__(self, root):
        self.size=300
        self.parent=root

        self.frameJam = Frame(root)

        self.buatFrameJam()
        self.buatJarum()
        self.buatTeksAngka()
        self.buatTeks()
        self.update_clock()

    def buatTeks(self):
        self.teks = Label(text="KELOMPOK 10")
        self.teks.pack()

    def buatFrameJam(self):
        root.title("Clock")
        self.w = Canvas(self.frameJam,width=320, height=320, relief= "sunken", border=0)
        self.w.pack()
        self.frameJam.pack()

    def buatJarum(self):
        self.w.create_line(0,0,0,0, fill="red", tags="hour", width=3)
        self.w.create_line(0,0,0,0, fill="black", tags="minute", width=6)
        self.w.create_line(0,0,0,0, fill="black", tags="second", width=6)

    def buatTeksAngka(self):
        Label(self.frameJam, text="12").place(x=160, y=13)
        Label(self.frameJam, text="11").place(x=80, y=28)
        Label(self.frameJam, text="10").place(x=31, y=90)
        Label(self.frameJam, text="9").place(x=11, y=157)
        Label(self.frameJam, text="8").place(x=31, y=230)
        Label(self.frameJam, text="7").place(x=80, y=285)
        Label(self.frameJam, text="6").place(x=160, y=303)
        Label(self.frameJam, text="5").place(x=240, y=285)
        Label(self.frameJam, text="4").place(x=291, y=230)
        Label(self.frameJam, text="3").place(x=310, y=157)
        Label(self.frameJam, text="2").place(x=291, y=90)
        Label(self.frameJam, text="1").place(x=240, y=28)

    def update_clock(self):
        s=time.localtime()[5]
        m=time.localtime()[4]
        h=time.localtime()[3]

        degrees = 6*s
        angle = degrees*pi*2/360
        ox = 165
        oy = 165
        x = ox + self.size*sin(angle)*0.45
        y = oy - self.size*cos(angle)*0.45
        self.w.coords("hour", (ox,oy,x,y))

        degrees1 = 6*m
        angle1 = degrees1*pi*2/360
        ox1 = 165
        oy1 = 165
        x1 = ox1 + self.size*sin(angle1)*0.4
        y1 = oy1 - self.size*cos(angle1)*0.4
        self.w.coords("minute", (ox1,oy1,x1,y1))

        degrees2 = 30*h
        angle2 = degrees2*pi*2/360
        ox2 = 165
        oy2 = 165
        x2 = ox2 + self.size*sin(angle2)*0.2
        y2 = oy2 - self.size*cos(angle2)*0.2
        self.w.coords("second",(ox2,oy2,x2,y2))

        self.parent.after(1000, self.update_clock)

root = Tk()
app = MyApp(root)
mainloop()
