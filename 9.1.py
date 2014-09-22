#-*- Coding:iso8859-15 -*-
def filexist(filename):
    try:
        f=open(filename,'r')
        f.close()
        return(1)
    except:
        return(0)
def lecturefichier(source):
    print("\n*****Début de fichier*****\n")
    if(filexist(source)):
        fichier=open(source,'r')
        while(1):
            txt=fichier.readline()
            if(txt==""):
                break
            else:
                print(txt)
        fichier.close()
    print("\n*****Fin de fichier*****")
flag=-1
while(flag!='Q'):
    flag=input("""-[L]ire le fichier\n-[M]odifier le fichier\n-[Q]uitter\n Votre choix:""")
    if(flag=="L"):
        source=input("\nNom du fichier:")
        lecturefichier(source)
    elif(flag=="M"):
        source=input("\nNom du fichier:")
        lecturefichier(source)
        fichier=open(source,'a')
        print("***Écrivez les lignes à ajouter***")
        ligne=0
        while(1):
            texte=input("Ligne "+str(ligne)+": ")
            ligne+=1
            if(texte==""):
                break
            else:
                fichier.write("\n"+texte)
        fichier.close()
        
