#!/usr/bin/env python3

from control_puertas import smart_locker_control as door

from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
from tkinter import messagebox
from read_qr import read_qr_sensor
def event_click_status(number):
    
        messagebox.showinfo('Message title', door.status_door(number))

def event_click_qr(status):
    
        messagebox.showinfo('Message title', str(read_qr_sensor.serial_read_qr(status)))


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Control de puertas")

        Style().configure("TButton", padding=(0, 7, 0, 5),
            font='serif 20')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)

        
        cls = Button(self, text="Puerta 1", command=lambda :door.open_door(1))
        cls.grid(row=1, column=0)
        bck = Button(self, text="Puerta 2", command=lambda :door.open_door(2))
        bck.grid(row=1, column=1)
        lbl = Button(self, text='Puerta 3', command=lambda :door.open_door(3))
        lbl.grid(row=1, column=2)
        sev = Button(self, text="puerta 4", command=lambda :door.open_door(4))
        sev.grid(row=2, column=0)
        eig = Button(self, text="puerta 5", command=lambda :door.open_door(5))
        eig.grid(row=2, column=1)
        nin = Button(self, text="puerta 6", command=lambda :door.open_door(6))
        nin.grid(row=2, column=2)

        div = Button(self, text="Estado puerta 1", command=lambda :event_click_status(1))
        div.grid(row=3, column=0)
        fou = Button(self, text="Estado puerta 2", command=lambda :event_click_status(2))
        fou.grid(row=3, column=1)
        fiv = Button(self, text="Estado puerta 3", command=lambda :event_click_status(3))
        fiv.grid(row=3, column=2)

        six = Button(self, text="Estado puerta 4", command=lambda :event_click_status(4))
        six.grid(row=4, column=0)
        mul = Button(self, text="Estado puerta 5", command=lambda :event_click_status(5))
        mul.grid(row=4, column=1)
        one = Button(self, text="Estado puerta 6", command=lambda :event_click_status(6))
        one.grid(row=4, column=2)

        two = Button(self, text="Estado todas las puertas", command=lambda :event_click_status('all'))
        two.grid(row=5, column=0)
        thr = Button(self, text="Abrir todas las puertas", command=lambda :door.open_door('all'))
        thr.grid(row=5, column=2)


        qr = Button(self, text="Escanear QR", command=lambda :event_click_qr(True))
        qr.grid(row=6, column=1)
       
        self.pack()


def main():
    
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("%sx%s"%(screen_width, screen_height))
    #root.geometry("300x600")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()