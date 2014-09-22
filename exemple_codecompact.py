from tkinter import *
fen1= Tk()

#création de widgets Label(), Entry() et Checkbutton():

Label(fen1, text='Premier champ:').grid(sticky=E)
Label(fen1, text='Deuxième:').grid(sticky=E)
Label(fen1, text='Troisième:').grid(sticky=E)

entr1=Entry(fen1)
entr2 = Entry(fen1)
entr3=Entry(fen1)
entr1.grid(row=0, column=1)
entr2.grid(row=1, column=1)
entr3.grid(row=2, column=1)
chek1=Checkbutton(fen1, text='Case à cocher, pour voir')
chek1.grid(columnspan=2)

#Création d'un widget Canvas contenant une image bitmap:
can1=Canvas(fen1, width=150, height=150, bg='white')
photo=PhotoImage(file='martin.gif')
can1.create_image(80,80, image=photo)
can1.grid(row=0,column=2, rowspan=4, padx=10, pady=5)

fen1.mainloop()
