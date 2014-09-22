#Écrivz un petit programme qui crée une nouvelle liste t3 en les alternant pour que mois puis date
t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['Janvier','Février', 'mars', 'Avril', 'Mai', 'Juin', 'juillet', 'Aot','Septembre','Octobre','Novembre','Décembre']
t3=[]
i=0
while i<len(t2):
    t3.append(t2[i])
    t3.append(t1[i])
    i+=1
print(t3)
#exercice 5.12 : Afficher la liste proprement
i=0
while i<len(t2):
    print(t2[i], end=', ')
    i+=1
#exercice 5.13 :rechercher la plus grosse valeur de la liste
t4=[32,5,12,8,3,75,2,15]
biggest=0
i=0
while(i<len(t4)):
    if(t4[i]>biggest):
        biggest=t4[i]
    i+=1
print(biggest)
#exercice 5.14 trier les pairs impairs, utilisation de la liste t4
i=0
pairs=[]
impairs=[]
while(i<len(t4)):
    if((t4[i]%2)==0):
        pairs.append(t4[i])
    else:
        impairs.append(t4[i])
    i+=1
print(pairs, end=", ")
print(impairs, end=", ")

