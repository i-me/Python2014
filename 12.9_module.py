class CompteBancaire(object):
    "Compte en banque"
    def __init__(self, nom="Dupont", solde=1000):
        self.nom=nom   #valeur par défaut du nom
        self.solde=solde     #valeur par défaut du solde
    def depot(self, somme):
        self.solde+=somme
    def retrait(self, somme):
        self.solde-=somme
    def affiche(self):
        print("Le compte de M.{0}, a un solde de {1}$".format(self.nom, self.solde))
class CompteEpargne(CompteBancaire):
    def __init__(self, tauxInteret=0.3):
        CompteBancaire.__init__(self)
        self.tauxInteret=tauxInteret/100
    def changeTaux(self, tauxInteret):
        self.tauxInteret=tauxInteret/100
    def capitalisation(self, nombreMois):
        print("Le taux d'intérêt {0} sera appliqué pendant {1} au compte épargne".format(self.tauxInteret*100, nombreMois))
        i=0
        for i<nombreMois:
            self.solde+=self.solde*self.tauxInteret
            i++
if __name__=="__main__":
    compte1=CompteBancaire("Duchmol", 800)
    compte1.depot(350)
    compte1.retrait(200)
    compte1.affiche()
