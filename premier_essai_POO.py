#Définition d'une classe de facons classique sans faire de méthode
class Time(object):
    "Définition d'un objet temporel"
    def __init__(self, hh=12, mm=0, ss=0):
        self.heure=hh
        self.minute=mm
        self.seconde=ss
    def afficher_heure(self):
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))
instant=Time(22)
#instant.heure=12
#instant.minute=40
instant.seconde=25
instant.afficher_heure()
