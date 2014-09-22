from turtle import *
def carre(angle=0,couleur="blue",coter=25):
    "Dessine un carré à un certains angle"
    angleCarre=90
    forward(coter)
    down()
    left(angle)
    color(couleur)
    left(angleCarre)
    forward(coter)
    left(angleCarre)
    forward(coter)
    left(angleCarre)
    forward(coter)
    left(angleCarre)
    forward(coter)
    up()
def triangle(angle=0,couleur="red",coter=25):
    "Dessine un triangle à un certains angle"
    forward(coter)
    down()
    left(angle)
    color(couleur)
    left(120)
    #forward(coter)
    forward(coter)
    left(120)
    forward(coter)
    left(120)
    forward(coter)
    up()
