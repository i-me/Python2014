class satellite(object):
    "Definition d'un satellite"
    def __init__(self, nom="Expérimental", masse=100, vitesse=0):
        self.nom=nom
        self.force=0
        self.vitesse=vitesse
        self.duree=0
        self.masse=masse
    def impulsion(self):
        #calcul de l'augmentation de la vitesse DELTA V
        print("--Calcul de l'augmentation de la vitesse DELTA V\n")
        dvitesse=(self.force*self.duree)/self.masse
        print("--Impulsion donnant une augmentation de vitesse de ",dvitesse,"m/s\n")
        self.vitesse+=dvitesse
        print("Vitesse finale",self.vitesse,"m/s\n")
    def affiche_vitesse(self):
        print("La vitesse du satellite ", self.nom," est de ", self.vitesse,"m/s")
    def energie(self):
        #calcul de l'energie cinetique e=mv2/2
        ecinetique=(self.masse*(self.vitesse)**2)/2
        print("--Calcul de l'énergie cinétique e=m(v^2)/2\n")
        print("Énergie cinétique du satellite", ecinetique)


gallileo=satellite("Galliléo", masse=300)

message="Veuillez saisir la {0} du satellite {1}: "
gallileo.masse=int(input(message.format("masse en KG ", gallileo.nom)))
gallileo.duree=int(input (message.format(" duree de l'impulsion en secondes", gallileo.nom)))
gallileo.force=int(input(message.format(" force de l'impulsion en Newton", gallileo.nom)))
print(gallileo.force, gallileo.duree)
gallileo.impulsion()
gallileo.affiche_vitesse()
gallileo.energie()

