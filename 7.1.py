#-*- Coding:iso8859-15 -*-
#Exercice 7.1, importer turtle pour effectuer des dessinss simples
#Utiliser des fonctions pour préprogrammer un triangle
from turtle import *
def triangle(x,y,cote,couleur="blue"):
    up()
    goto(x,y)
    down()
    color(couleur)
    forward(cote)
    left(120)
    forward(cote)
    left(120)
    forward(cote)
    

def plusieursTrianglesAlignes(nbTriangle,cote, couleur="blue", x=0, y=0):
    a=1
    while(a<=nbTriangle):
        triangle(x,y,cote,couleur)
        x=x+cote
        a=a+1

plusieursTrianglesAlignes(24,30,"red",-300)


