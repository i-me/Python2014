from tkinter import *
#def dessine_rond(x1,y1,r,couleur):
 #   "Dessine des ronds d'une taille spécifique dans le canvas"
def create_Canvas():
    global can1
    global fen1
    can1=Canvas(fen1,bg="dark grey", height=canvasHeight, width=canvasWidth)
def laCroix():
    can1.create_line(0,canvasHeight/2,canvasWidth, canvasHeight/2, width=2, fill="red")
    can1.create_line(canvasWidth/2,0,canvasWidth/2,canvaHeight,width=2,fill="red")
    
    
