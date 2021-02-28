from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("515x160")


label = Label(app_window,fg = "blue",bg = "black",font = "Verdana 68 bold",bd=25)
label.grid(row=0,column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)

digital_clock()
app_window.mainloop()
