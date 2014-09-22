#-*- Coding:iso8859-15 -*-
from math import *

#distancemile=input("Distance en miles:")
distancemile=3
distancekm=float(distancemile)*1.609
print(round(distancekm,4))

#6.2, écrivez un programme qui calcule le périmètre et l'aire d'un triangle quelqconque dont l'utilisateu fournit les 3 côtés
#a=float(input("Coté #1 du triangle:"))
#b=float(input("Coté #2 du triangle:"))
#c=float(input("Coté #3 du triangle:"))
a,b,c=1,2,3
perimetre=a+b+c
dperim=perimetre/2
aire=sqrt(dperim*(dperim-a)*(dperim-b)*(dperim-c))
print("Le périmètre du triangle est ",perimetre,", son aire est de ",round(aire,4))

#6.4 boucle de saisie avec insertion de valeurs dans un tableau
#retour=[]
#stop=0
#while(stop!=1):
 #   retour.append(input("Veuillez entrer une valeur:"))
  #  if(retour[len(retour)-1]==""):
   #     del(retour[len(retour)-1])
    #    stop=1
#print(retour)
#Faisont mumuse avec turtle
from turtle import *
color("green")
forward(100)
left(60)
color("blue")
forward(100)
left(60)
color("red")
forward(100)
left(67.5)
