from tkinter import *
from tkinter import ttk
class mengubahJudul(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")

        self.tampilan = parent

        self.initUI()
      

    def initUI(self):
        self.tampilan.title("Aplikasi FPB dan KPK")
        self.pack(fill=BOTH, expand=1)
        self.tampilan.geometry("640x480+300+300")



root = Tk()
app = mengubahJudul(root)
root.mainloop()
