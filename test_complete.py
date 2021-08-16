#!/usr/bin/env python3

from control_puertas import smart_locker_control as door

from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
from tkinter import messagebox
def event_click_status(number):
    
        messagebox.showinfo('Message title', door.status_door(number))

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Control de puertas")

        Style().configure("TButton", padding=(0, 3, 0, 3),
            font='serif 30')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        cls = Button(self, text="Puerta 1", command=lambda: door.open_door(1))
        cls.grid(row=1, column=0)
        bck = Button(self, text="Puerta 2", command=lambda: door.open_door(2))
        bck.grid(row=1, column=1)
        lbl = Button(self, text='Puerta 3', command=lambda: door.open_door(3))
        lbl.grid(row=1, column=2)
        clo = Button(self)
        clo.grid(row=1, column=3)
        sev = Button(self, text="puerta 4", command=lambda: door.open_door(4))
        sev.grid(row=2, column=0)
        eig = Button(self, text="puerta 5", command=lambda: door.open_door(5))
        eig.grid(row=2, column=1)
        nin = Button(self, text="puerta 6", command=lambda: door.open_door(6))
        nin.grid(row=2, column=2)
#         div = Button(self)
#         div.grid(row=2, column=3)
# 
        fou = Button(self, text="Estado puerta 1", command=lambda: event_click_status(1))
        fou.grid(row=3, column=0)
        fiv = Button(self, text='Estado puerta 2', command=lambda: event_click_status(2))
        fiv.grid(row=3, column=1)
        six = Button(self, text='Estado puerta 3', command=lambda: event_click_status(3))
        six.grid(row=3, column=2)
        mul = Button(self, text="Estado puerta 4", command=lambda: event_click_status(4))
        mul.grid(row=3, column=3)
# 
        one = Button(self, text="Estado puerta 5", command=lambda: event_click_status(5))
        one.grid(row=4, column=0)
        two = Button(self, text="Estado puerta 6", command=lambda: event_click_status(6))
        two.grid(row=4, column=1)
#         thr = Button(self)
#         thr.grid(row=4, column=2)
#         mns = Button(self)
#         mns.grid(row=4, column=3)
# 
#         zer = Button(self)
#         zer.grid(row=5, column=0)
#         dot = Button(self)
#         dot.grid(row=5, column=1)
#         equ = Button(self)
#         equ.grid(row=5, column=2)
        pls = Button(self, text='abrir todas', command=lambda: door.open_door('all'))
        pls.grid(row=5, column=3)

        self.pack()


def main():
    
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("%sx%s"%(screen_width, screen_height))
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()