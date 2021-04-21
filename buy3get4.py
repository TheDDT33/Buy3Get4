# Buy 3 Get 4
from tkinter import *

GUI = Tk()
GUI.geometry('400x450')

F1 = Frame(GUI)
F1.pack()

FONT1 = (None,25)

L0 = Label(F1, text='ราคาต่อคน', font=FONT1)
L0.pack()

v_price = StringVar()
E1 = Entry(F1, textvariable=v_price, font=FONT1, justify='center')
E1.pack()

L1 = Label(F1, text='จำนวนคน', font=FONT1)
L1.pack()

v_ea = StringVar()
E2 = Entry(F1, textvariable=v_ea, font=FONT1, justify='center')
E2.pack()

L2 = Label(F1,text='ราคารวมทั้งหมด', font=FONT1)
L2.pack()

v_total = StringVar()
L2 = Label(F1, textvariable=v_total, font=FONT1, fg='BLUE')
L2.pack()

def Total(event=None):
    price =int(v_price.get())
    ea = int(v_ea.get())

    if ea >= 4 and ea < 8:
        total = price * (ea-1)
    elif ea >=  8 and ea < 12:
        total = price * (ea-2)
    elif ea >= 12 and ea < 14:
        total = price * (ea-3)
    elif ea >=  14 and ea < 16:
        total = price * (ea-4)
    else :
        total = price * ea
        
    v_price.set('')
    v_ea.set('')
    E1.focus()

    return v_total.set(total)

GUI.bind('<Return>',Total)

B1 = Button(F1, text='START', font=FONT1, command=Total)
B1.pack()

GUI.mainloop()
