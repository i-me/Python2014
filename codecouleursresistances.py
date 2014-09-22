class Application(object):
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root = Tk()
        self.root.title('code des couleurs')
        self.dessineResistance()
        Label(self.root, text="Entrez la valeur de la résistance, en ohms :").\
                         grid(row=2, column=1, columnspan=3)
        #Button(self.root, text='Montrer', command=self.changeCouleurs).\
         #                 grid(row=3, column=1)
        Button(self.root, text='Quitter', command=self.root.destroy).\
                          grid(row=3, column=3)
        self.entree=Entry(self.root, width=14)
        self.entree.bind("<Return>",self.changeCouleurs)
        self.entree.grid(row=3, column=2)
        #Code des couleurs pour les valeurs de zéro à neuf:
        self.cc=['black','brown','red','orange','yellow','green','blue','purple','grey','white']
        self.root.mainloop()
    def dessineResistance(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.can=Canvas(self.root, width=250, height=100, bg='light blue')
        self.can.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
        self.can.create_line(10,50,240,50,width=2)
        self.can.create_rectangle(65,30,185,70, fill='beige', width=2)
        #Dessin des trois lignes colorées (noires au départ):
        self.ligne=[]
        for x in range(85,150,30):
            self.ligne.append(self.can.create_rectangle(x,30,x+20,70,fill='black',width=0))
    def changeCouleurs1(self, event):
        self.changeCouleurs()
    def changeCouleurs(self, event):
         """Affichage des couleurs correspondant à la valeur entrée"""
         self.v1ch=self.entree.get() #cette méthode renvoie une chaine
         try:
             v=float(self.v1ch) #conversion en valeur numérique
         except:
             err=1 #erreur: entrée non numérique
         else:
             err=0
         if err==1 or v < 10 or v > 1e11:
             self.signaleErreur() #entrée incorrecte ou hors limites
         else:
             li=[0]*3 #liste des 3 codes à afficher
             logv = int(log10(v)) #partie entière du logarithme
             ordgr = 10**logv #partie entière du logarithme
             #extraction du premier chiffre significatif
             li[0]=int(v/ordgr) #partie entière
             decim = v/ordgr - li[0] #partie décimale
             #extraction du second chiffre significatif:
             li[1]=int(decim*10+.5) #+.5 pour arrondir correctement
             #nombre de zéros à accoler aux 2 chiffres significatifs:
             li[2]=logv -1
             #coloration des 3 lignes:
             for n in range(3):
                 self.can.itemconfigure(self.ligne[n], fill=self.cc[li[n]])
    def signaleErreur(self):
        self.entree.configure(bg='red')
        self.root.after(1000,self.videEntree)

    def videEntree(self):
        self.entree.configure(bg='white')       #rétablir le fond blanc
        self.entree.delete(0,len(self.v1ch)) #enlever les car. présents
if __name__ == '__main__':
    from tkinter import *
    from math import log10
    f=Application()
                
