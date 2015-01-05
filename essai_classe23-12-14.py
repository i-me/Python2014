import math
def distance(p,p2):
    "Calcul de la distance entre les 2 coordonnées fournises"
    valeur=((p2.x-p.x)**2)+((p2.y-p.y)**2)
    valeur=math.sqrt(valeur)
    maphrase="Distance entre le point A et B est : "+ str(int(valeur))
    return maphrase
class Point(object):
    "Contient les points du graphique"
p1=Point()
p1.x=1
p1.y=2
p2=Point()
p2.x=4
p2.y=6
print (distance(p1,p2))
