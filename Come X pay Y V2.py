# COME x PAY y
from tkinter import *

GUI = Tk()
GUI.geometry('450x300')

F1 = Frame(GUI)
F1.pack()

FONT1 = (None,25)

L1 = Label(F1, text='ระบุโปรโมชั่น', font=(None,30))
L1.pack()

############################

L2 = Label(F1, text='มา', font=FONT1)
L2.pack(side=LEFT)

v_come_x = StringVar()
E1 = Entry(F1, textvariable=v_come_x, font=FONT1, width=3, justify='center')
E1.pack (side=LEFT)

v_pay_y = StringVar()
E2 = Entry(F1, textvariable=v_pay_y, font=FONT1, width=3, justify='center')
E2.pack (side=RIGHT)

L3 = Label(F1, text='จ่าย', font=FONT1)
L3.pack(side=RIGHT)


###############################
F2 = Frame(GUI)
F2.pack()

L4 = Label(F2, text='-----------------------------', font=FONT1)
L4.pack()

L5 = Label(F2, text='ราคาต่อคน', font=FONT1)
L5.pack(side=LEFT)

v_per_head = StringVar()
E3 = Entry(F2, textvariable=v_per_head, font=FONT1, width=3, justify='center')
E3.pack (side=LEFT)

v_pax = StringVar()
E4 = Entry(F2, textvariable=v_pax, font=FONT1, width=3, justify='center')
E4.pack (side=RIGHT)

L6 = Label(F2, text='จำนวนคนที่มา', font=FONT1)
L6.pack(side=RIGHT)
###############################
F3 = Frame(GUI)
F3.pack()

L7 = Label(F3, text='-----------------------------', font=FONT1)
L7.pack()

v_total = StringVar()
L8 = Entry(F3, textvariable=v_total, font=(None,35), width=15, justify='center')
L8.pack ()

def Total(event=None):
    come_x = int(v_come_x.get())
    pay_y = int(v_pay_y.get())
    per_head = int(v_per_head.get())
    pax = int(v_pax.get())

    total = ((pax % come_x) * per_head) + (pax // come_x) * (pay_y * per_head)

    v_per_head.set('')
    v_pax.set('')

    return v_total.set(total)

GUI.bind('<Return>',Total)

B1 = Button(F3, text='START', font=FONT1, command=Total)
B1.pack(side=BOTTOM)

GUI.mainloop()
