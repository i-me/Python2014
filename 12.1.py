class Domino(object):
    "Classe contenant le domino"
    def __init__(self, faceA=0, faceB=0):
        self.faceA=faceA
        self.faceB=faceB
    def affiche_points(self):
        return("\nface A:{0}  face B:{1}".format(self.faceA, self.faceB))
    def valeur(self):
        return(self.faceA+self.faceB)
d1=Domino(2,6)
d2=Domino(4,3)
print(d2.faceA, d2.faceB, d1.affiche_points())
print("total des points:", d1.valeur()+d2.valeur())
liste_dominos=[]
for i in range(7):
    liste_dominos.append(Domino(6,i))
print(liste_dominos[3])
