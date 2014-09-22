#-*- Coding:iso8859-15 -*-
from module_dessins import *
def laCroix(couleur="red"):
    can1.create_line(0,canvasHeight/2,canvasWidth, canvasHeight/2, width=2, fill=couleur)
    can1.create_line(canvasWidth/2,0,canvasWidth/2,canvasHeight,width=2,fill=couleur)
def effacerLaCroix():
    global couleurCanvas
    laCroix(couleur=couleurCanvas)
def dessinerCercle(x1=0,y1=0,r=0,couleur="blue"):
    "Dessine un cercle de rayon r"
    can1.create_oval(x1-r, y1-r, x1+r, y1+r, outline=couleur)
def dessin1(couleur="blue"):
    "Dessine une suite de cercle emboîté"
    global canvasHeight
    global canvasWidth
    x1=canvasHeight/2
    y1=canvasWidth/2
    i=0
    while (i<10):
        r=50+(20*i)
        dessinerCercle(x1,y1,r, couleur)
        i+=1
def effacerDessin1():
    dessin1(couleur=couleurCanvas)


fen1=Tk()
canvasHeight=600
canvasWidth=600
couleurCanvas="dark grey"
can1=Canvas(fen1,bg=couleurCanvas, height=canvasHeight, width=canvasWidth)
tex1=Label(fen1, text="Caneva #1", fg="red")
tex1.pack(side=TOP)
bou1=Button(fen1, text="Afficher croix", command=laCroix)
bou1.pack(side=RIGHT)
bou2=Button(fen1, text="Effaccer Croix", command=effacerLaCroix)
bou2.pack(side=RIGHT)
bou3=Button(fen1, text="Cercle", command=dessin1)
bou3.pack(side=BOTTOM)
bou4=Button(fen1, text="Effacer cercle", command=effacerDessin1)
bou4.pack(side=BOTTOM)
can1.pack(side=LEFT)
fen1.mainloop()
