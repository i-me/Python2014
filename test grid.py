from tkinter import *
fen1=Tk()
txt1=Label(fen1,text='Premier champ:')
txt2=Label(fen1, text='Second:')
entr1=Entry(fen1)
entr2=Entry(fen1)
txt1.grid(row=0)
txt2.grid(row=1)
entr1.grid(row=0, column=1)
entr2.grid(row=1,column=1)
          
fen1.mainloop()
