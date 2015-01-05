import math
class Cercle(object):
    "Cercles de taille variés"
    def __init__(self, rayon=1):
        self.rayon=rayon
    def surface(self):
        self.surface=math.pi*(self.rayon**2)
        return(self.surface)
    def affiche(self, donnee):
        return(round(donnee,2))
class Cylindre(Cercle):
    "Cylindre de taille variés dérivant de la class Cercle"
    def __init__(self, rayon=1, hauteur=1):
        self.rayon=rayon
        self.hauteur=hauteur
        Cercle.__init__(self,rayon)
    def volume(self):
        self.volume=Cercle.surface(self)*self.hauteur
        return(self.volume)
class Cone(Cylindre):#Exercice 12.6
    def __init__(self, rayon=1, hauteur=1):
        self.rayon=rayon
        self.hauteur=hauteur
        Cylindre.__init__(self, rayon, hauteur)
    def volume(self):
        self.volume=Cylindre.volume(self)/3#Pi*(r^2)=Surface cercle *h =volume cylindre. /3 = aire cylindre
        return(self.volume)
        
cercle1=Cercle(10)
print(cercle1.affiche(cercle1.surface()))
cylindre1=Cylindre(5,7)
print(cylindre1.affiche(cylindre1.surface()))
print(cylindre1.affiche(cylindre1.volume()))
co=Cone(5, 7)
print(co.affiche(co.volume()))

