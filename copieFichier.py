#-*- Coding:UTF-8 -*-
def copieFichier (source, destination):
    "Copie intégrale d'un fichier"
    fs=open(source, 'r')
    fd=open(destination,'w')
    while 1:
        txt=fs.read(50)
        if txt=="":
            break
        fd.write(txt)
    fs.close()
    fd.close()
copieFichier('source.log','destination')
