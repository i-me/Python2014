#-*- Coding:iso8859-15 -*-
#Calcul du nombre d'occurence d'une lettre donnée dans une chaîne
chaine="""eLorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur est arcu, pharetra at porta sit amet, condimentum ut felis. Proin faucibus gravida purus. Nullam vulputate nisi vitae erat varius, id faucibus ligula elementum. Donec nec tellus imperdiet, bibendum mauris at, feugiat nulla. Praesent ut fermentum tortor. Aliquam fermentum metus velit.e"""
i=0
carac="e"#Caractère à compter le nombre d'occurence
compte=0
while(i<len(chaine)):
    if(chaine[i]==carac):
        compte+=1
    i+=1
print(carac,"-",compte, "occurences")
    
