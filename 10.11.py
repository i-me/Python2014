#-*- Coding:iso8859-15 -*-
phrase="Bonjour je suis à la recherche d'un chien nommé Garis"
mot=""
chaine=[""]
i=0
for c in phrase:
    if c==" " or c=="":
        chaine.append("")
        i+=1
    else:
        chaine[i]+=c   
print(chaine)

