from tkinter import *

def cercle(can, x, y, r, coul="black"):
    "dessin d'un cercle de reayon <r> en <x,y> dans le canevas <can>"
    can.create_oval(x-r,y-r,x+r,y+r, fill=coul)
class Application(Tk):
    def __init__(self):
        Tk.__init__(self) #constructeur de la classe parente
        self.can=Canvas(self, width=475, height=130, bg="white")
        self.can.pack(side=TOP, padx=5, pady=5)
        Button(self, text="Train", command=self.dessine).pack(side=LEFT)
        Button(self, text="Hello", command=self.coucou).pack(side=LEFT)

    def dessine(self):
        "instanciation de 4 wagons dans le canevas"
        self.w1=Wagon(self.can, 10, 30) #Wagon --> Class que nous créerons qui fait des wagons selon les coordonées fournises
        self.w2 = Wagon(self.can, 130,30)
        self.w3=Wagon(self.can, 250, 30)
        self.w4=Wagon(self.can, 370, 30)
        self.w4.fenetre[1].configure(fill="black")

    def coucou(self):
        "apparition de personnages dans certaines fenêtres"
        self.w1.perso(3)
        self.w3.perso(1)
        self.w3.perso(2)
        self.w4.perso(1)
class Wagon(object):
    def __init__(self, canev, x,y):
        "dessin d'un petit wagon en <x,y> dans le canevas <canev>"
        #mémorisation des paramètres dans des variables d'instance
        self.canev, self.x, self.y=canev, x,y
        #rectangle de base : 95*60 px:
        canev.create_rectangle(x,y,x+96, y+60)
        #3 fenêtres de 25*40px écartées de 5px:
        self.fenetre=[]
        i=0
        for xf in range(x+5, x+90, 30):
            self.fenetre.append=canev.create_rectangle(xf, y+5, xf+25, y+40)
            print(self.fenetre)
        #2 roues de rayon égal à 12 px
        cercle(canev, x+18, y+73, 12, "grey")
        cercle(canev, x+77, y+73, 12, "grey")
    def perso(self, fen):
        "apparition d'un eptit personnge à la fenêtre <fen>"
        #calcul des coordonnnées du centre de chaque fenêtre:
        xf=self.x + fen*30-12
        yf=self.y+25
        cercle(self.canev, xf, yf, 10) #visage
        cercle(self.canev, xf-5, yf-3, 2) #oeil gauche
        cercle(self.canev, xf+5, yf-3, 2) #oeil droit
        cercle(self.canev, xf, yf+5, 3)
app=Application()
app.mainloop()
