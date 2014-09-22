#-*- Coding:iso8859-15 -*-
from turtle import *
from premierModule import *
#carre(95,"red",500)
#triangle(35,coter=90)
listeCoter=(25,50,35,70,45,90,50,100,55,110,60,120,65,130,70,140,75,150)
i=0
up()
goto(0,0)
while(i<len(listeCoter)):
    triangle(angle=25,coter=listeCoter[i])
    carre(angle=0,coter=listeCoter[i])
    i+=1
