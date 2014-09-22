from tkinter import *
from math import sin, pi

class OscilloGraphe(Canvas):
    "Canevas spécialis, pour dessiner des courbes élongation/temps"
    def __init__(self, boss=None, larg=200, haut=150):
        "Constructeur du graphique: axes et échelle horiz."
        #construction du widget parent:
        Canvas.__init__(self) #appel au constructeur
        self.configure(width=larg, height=haut)#de la classe parente
        self.larg, self.haut=larg, haut #mémorisation
        #tracé des axes de références:
        self.create_line(10, haut/2, larg, haut/2, arrow=LAST)#axe  X
        self.create_line(10, haut-5, 10, 5, arrow=LAST)#Remarquons arrow pour fleche
        #tracé d'une échelle avec 8 graduation:
        pas=(larg-25)/8. #intervalles de l'échelle horizontale
        for t in range(1, 9):
            stx=10+t*pas #+10 pour partir de l'Orgiinie
            self.create_line(stx, haut/2-4, stx, haut/2+4)

    def traceCourbe(self, freq=1, phase=0, ampl=10, coul='red'):
        "Tracé d'un graphique élongation/temps sur 1 seconde"
        curve=[] #liste des coordonnées
        pas=(self.larg-25)/1000.
        for t in range(0,1001, 5):#l'échelle X correspond à 1 seconde
            e=ampl*sin(2*pi*freq*t/1000-phase)
            x=10+t*pas
            y=self.haut/2-e*self.haut/25
            curve.append((x,y))
           
        n=self.create_line(curve, fill=coul, smooth=1) #n=numéro d'ordre du tracé (self.create_line puisque une class canvas)
        return n
###Code pour tester la class :###
if __name__== '__main__':
    root=Tk()
    gra=OscilloGraphe(root, 250, 180)
    gra.pack()
    gra.configure(bg='ivory', bd=2, relief=SUNKEN)
    gra.traceCourbe(2,1.2,10,coul='purple')
    root.mainloop()
