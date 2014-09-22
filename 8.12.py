from tkinter import *
from math import *

def deplacer(objet, x,y):
    global x1, y1, x2,y2
    if objet==oval1:
        x1, y1=x1+x, y1+y
        can1.coords(objet, x1, y1, x1+30, y1+30)
    else:
        x2,y2=x2+x, y2+y
        can1.coords(objet, x2,y2,x2+30, y2+30)
    distance()

def distance():
    #On calcule le centre de tous les cercles, x, y, puis on utilise la formule pour obtenir distance
    centre_oval1=[can1.coords(oval1)[2]-15,can1.coords(oval1)[3]-15]
    centre_oval2=[can1.coords(oval2)[2]-15,can1.coords(oval2)[3]-15]
    distance=sqrt(((centre_oval2[0]-centre_oval1[0])**2)+(centre_oval2[1]-centre_oval1[1])**2)
    #print(centre_oval1, centre_oval2)#Test des données pour idle. Invisible à l'user
    label1.configure(text="Distance entre les deux planètes: "+str(round(distance, 3))+"")#mise en forme de la sortie

#Définition barbare des déplacement
def droite_oval1():
    deplacer(oval1, 20, 0)
def gauche_oval1():
    deplacer(oval1,-20, 0)
def haut_oval1():
    deplacer(oval1,0,-20)
def bas_oval1():
    deplacer(oval1,0,20)
def droite_oval2():
    deplacer(oval2, 20, 0)
def gauche_oval2():
    deplacer(oval2,-20, 0)
def haut_oval2():
    deplacer(oval2,0,-20)
def bas_oval2():
    deplacer(oval2,0,20)
    
fen1=Tk()
x1, y1= 10, 10
x2, y2= 180, 10
can1=Canvas(bg='darkgrey', height=300, width=300)
#On cree les planetes
oval1=can1.create_oval(x1,y1,x1+30,y1+30, width=2, fill="blue")
oval2=can1.create_oval(x2,y2,x2+30,y2+30, width=2, fill="red")
Button(fen1, text="Droite-Bleu", command=droite_oval1).grid(column=1)
Button(fen1, text="Gauche-Bleu", command=gauche_oval1).grid(column=1)
Button(fen1, text="Haut-Bleu", command=haut_oval1).grid(column=1)
Button(fen1, text="Bas-Bleu", command=bas_oval1).grid(column=1)

Button(fen1, text="Droite-Rouge", command=droite_oval2).grid(column=1)
Button(fen1, text="Gauche-Rouge", command=gauche_oval2).grid(column=1)
Button(fen1, text="Haute-Rouge", command=haut_oval2).grid(column=1)
Button(fen1, text="Bas-Rouge", command=bas_oval2).grid(column=1)


#Notre label
label1=Label(fen1)
label1.grid(column=0, columnspan=2)
distance()
can1.grid(row=0, column=0, rowspan=8)

fen1.mainloop()



