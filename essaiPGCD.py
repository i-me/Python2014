i=1
nbr1=12
nbr2=15
plusPetit=nbr2
plusGrand=nbr1
if(nbr1<nbr2):
    plusPetit=nbr1
    plusGrand=nbr2

pgcd=1
while((i<=plusPetit)):
    if((plusPetit%i)==0and(plusGrand%i)==0):
        pgcd=i
    i=i+1
print(pgcd)
