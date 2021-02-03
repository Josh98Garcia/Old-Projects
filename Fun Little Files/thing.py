import tkinter as tk
import time
import os

root = tk.Tk()
root.overrideredirect(True)

frameCnt = 169
frames = [tk.PhotoImage(file='startup.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", 'white')
    root.config(bg='white')
    root.after(40, update, ind)
label = tk.Label(root)
label.config(bg='white')
label.pack()
root.after(0, update, 0)
root.mainloop()