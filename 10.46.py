dictionnaire={
    "computer":"ordinateur",
    "mouse":"souris",
    "screen":"moniteur",
    "staple":"agrafeuse",
    "coffee":"café",
    "sex":"sexe"}
ndicto={}
for n in dictionnaire:
    ndicto[dictionnaire[n]]=n
chaine="Liste 1: {} \n Liste 2: {}"
print(chaine.format(dictionnaire,ndicto))
