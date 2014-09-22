from tkinter import *
def cree_cercle(x,y):
    cadre.create_oval(x-5,y-5,x+5,y+5,fill="red")
def pointeur(event):
    chaine.configure(text="click detecté en X="+str(event.x)+",Y="+str(event.y))
    cree_cercle(event.x,event.y)
fen=Tk()
cadre=Canvas(fen, width=200, height=150, bg="light yellow")
cadre.bind("<Button-1>",pointeur)
cadre.pack()
chaine=Label(fen)
chaine.pack( )

fen.mainloop()

            
