from tkinter import *

def changer():
    global c1, c2
    if(c1=="dark green"):
        c1, c2="red", "dark green"
    else:
        c1, c2="dark green","red"
    can1.itemconfigure(lumiere1, fill=c1)
    can1.itemconfigure(lumiere2, fill=c2)
    can1.itemconfigure(lumiere3, fill=c2)
    can1.itemconfigure(lumiere4, fill=c1)

fen1=Tk()

can1=Canvas(bg="light grey", width=1000, height=1000)
#Mise en place de la rue
can1.create_rectangle(100,0,920,1000, fill="dark grey")#Notre rue
x1,x2,y1,y2=100, 100, 300,700
while (x2<870):#Nos bandes jaunes répétitives
    x1,x2,y1,y2=x2+20, x2+40, 300, 700
    can1.create_rectangle(x1,y1,x2,y2, fill="yellow")
c1, c2="red", "dark green"
lumiere1=can1.create_oval(40,280, 80, 320, fill=c1)
lumiere2=can1.create_oval(40,680, 80,720, fill=c2)
lumiere3=can1.create_oval(940,280, 980, 320, fill=c2)
lumiere4=can1.create_oval(940,680, 980,720, fill=c1)
#fin mise en place de la rue

Button(text="Changer", command=changer).grid(column=1)
can1.grid(row=0, column=0)
fen1.mainloop()
