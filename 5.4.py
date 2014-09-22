#-*- Coding:iso8859-15 -*-
taux=0.043#%/100
interets=0#Montant des intérêts
montant=100
temps=20#Temps en année
i=0
while(i<temps):
    interets=taux*montant
    print(i,"année, Intérêts de ", round(interets,2), "€, sur un montant de ", round(montant,2))
    montant+=interets
    i+=1


