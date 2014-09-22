class compte(object):
    "compte bancaire"
    def __init__(self, montant = 0, nom="Défaut"):
        self.solde=montant
        self.nom=nom
    def depot(self, montant=0):
        self.solde=self.solde+montant
        print("--Dépôt de ",montant,"$ effecturé au compte ",self.nom, "-- Solde :", self.solde, "$\n")
    def retrait(self, montant=0):
        self.solde=self.solde-montant
        print("--Retrait de", montant,"$ effectué au compte", self.nom,"-- Solde:", self.solde, "$\n")
    def transfert(self, destination, montant=0):
        if(montant<self.solde):
            destination.depot(montant)
            self.retrait(montant)
        else:
            print("Montant non disponible au compte")
compte1=compte(1400, "Principal")
compte2=compte(30, "Épargne")
compte1.depot(14)
compte1.transfert(compte2, 12)
print(compte1.solde, compte2.solde)
