#!/usr/local/bin/python3

try:
    from tkinter import *
except:
    from Tkinter import *
import time
import os

text="Look at an Object\n 20 Feets away\n For 20 seconds"

Time = time.strftime("%I:%M %p", time.localtime())

dir_path = os.path.dirname(os.path.realpath(__file__))
log_file = os.path.join(dir_path, 'eye-saver.log')
f = open(log_file,'a')
f.write(Time + ': ' + 'Eye Saver script executed\n')
f.close()

def display():
    l.config(text=text, fg="black")
    root.after(100, display)

root = Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.after(20000, lambda: root.destroy())
root.lift()
root.call('wm', 'attributes', '.', '-topmost', '1')
#root.bind('<Escape>', exit)

l = Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

b = Button(root, text="Close", command=exit)
b.pack(anchor='se')

display()
root.mainloop()
