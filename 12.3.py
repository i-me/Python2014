class Voiture(object):
    "Une voiture"
    def __init__(self, marque="Ford", couleur="Rouge", ):
        self.marque=marque
        self.couleur=couleur
        self.pilote="Personne"
        self.vitesse=0
    def choixConducteur(self, nom):
        self.pilote=nom
    def accelerer(self, taux, duree):
        if(self.pilote!="Personne"):#Il y a un conducteur
            self.vitesse+=(int(taux)*int(duree))
            return(self.vitesse)#retourne la vitesse en M/s
        else:
            return("Il n'y a pas de conducteur. Accélération impossible")
    def afficher_tout(self):
        chaine="L'auto de {0} est une {1} de couleur {2} allant à une vitesse de {3}m/s"
        print(chaine.format(self.pilote, self.marque, self.couleur, self.vitesse))
voiture1=Voiture("Nissan", "Bleu")
print(voiture1.accelerer(10, 10))

voiture1.choixConducteur("Raoul")
print(voiture1.accelerer(10, 10))
voiture1.afficher_tout()
