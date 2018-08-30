#!/usr/bin/python3

try:
    from tkinter import *
except:
    from Tkinter import *
import sys
#import webbrowser
#import random
#import time

root = Tk()
text="Look at an Object\n 20 feet away\n for 20 seconds"

#videos = ('https://www.youtube.com/watch?v=GSO6g3dNR7s',
#'https://www.youtube.com/watch?v=Y2dHYfb5OnE',
#'https://www.youtube.com/watch?v=uiKg6JfS658',
#'https://www.youtube.com/watch?v=azCzW_0GADM')

#webbrowser.open(random.choice(videos))

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


frame = Frame(root, bd=1, relief=GROOVE)
frame.grid()
#video.attach_window(frame.window_id())

Label(frame, text=text, fg="red", font=("Helvetica", 24), anchor=CENTER, justify=CENTER).grid()
#Button(frame, text="Close", command=exit).grid(row=1, column=1)

center(root)
root.title("Eye Saver: Tool to Saver Vision")
#root.attributes("-fullscreen", True)
root.bind('<Escape>', exit)
root.after(20000, lambda: root.destroy())
root.mainloop()



