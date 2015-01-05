class Satellite(object):
    def __init__(self, nom="NO-NAME", masse=100, vitesse=0):
        self.nom=nom
        self.masse=masse
        self.vitesse=vitesse
        self.energieC()
    def impulsion(self, force, duree):
        self.vitesse+=((force*duree)/self.masse)
        self.energieC()
    def affiche_vitesse(self):
        print("Le satellite {0} a une vitesse de {1}m/s".format(self.nom, self.vitesse))

    def energieC(self):
        eC=((self.masse)*(self.vitesse**2))/2
        self.energie=eC
s1=Satellite('Zoé',masse=250, vitesse=10)
s1.impulsion(500,15)
s1.affiche_vitesse()
print(s1.energie)
s1.impulsion(500,15)
s1.affiche_vitesse()
print(s1.energie)
