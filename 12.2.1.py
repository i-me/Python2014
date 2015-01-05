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

compte1=CompteBancaire("Duchmol", 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
