#-*- Coding:iso8859-15 -*-
from tkinter import *
def createCarre(coordonnes,couleur):
    can1.create_rectangle(coordonnes[0],coordonnes[1],coordonnes[2],coordonnes[3],color=couleur)

def createDamier():
    x,y,y2,col=0,0,75,0
    i=0#itérateur
    global coordonnee_x
    i2=0#itérateur de nombre colone
    coordonnee_x=[[0,0]]
    while(i<10):#Nombre de ligne
        while(i2<10):#Nombre de colone
            xS=[coordonnee_x[i2][1],coordonnee_x[i2][1]+75]
            coordonnee_x.append(xS)
            if col>0:
                couleur="blue"
                col=0
            else:
                couleur="white"
                col=1
            can1.create_rectangle(xS[0],y,xS[1],y2, fill=couleur)
            i2+=1

            "Passage en boucle pour chaque ligne"
            print(coordonnee_x)
            y,y2=y2,y+75
            i+=1
coordonnee_x=[]
fen1=Tk()
can1=Canvas(fen1, bg="dark grey", width=800, height=800)
bou1=Button(fen1, text="Cree Damier", command=createDamier)
bou1.pack(side=BOTTOM)
can1.pack(side=TOP, pady=20)
fen1.mainloop()


        
    
    
