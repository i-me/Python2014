class JeuDeCartes(object):
    "Instanciation de nouvel object similaire à un jeu de cartes"
    def __init__(self):
        "Instanciation du paquet de cartes"
        self.paquet=[]
        self.valeursCartes=[2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.couleurCartes=[3,2,1,0]
        for c in self.couleurCartes:
            for v in self.valeursCartes:
                self.paquet.append((v,c))
    def nom_carte(self, carte=(2,0)):
        "Retourne le nom de la carte pigé"
        valeursCartes_absolut=[2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi", "As"]
        #print(valeursCartes_absolut[carte[0]-2])
        couleurCartes_absolut=["Pique", "Trèfle", "Carreau", "Coeur"]
        return("{0} de {1}".format(valeursCartes_absolut[carte[0]-2],couleurCartes_absolut[carte[1]]))
    def battre(self):
        "Bat le paquet de carte"
        
paquet=JeuDeCartes()
print(paquet.nom_carte((14,3)))
        
