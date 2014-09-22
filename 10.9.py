#-*-Coding:iso8859-15-*-
def verif_nombre(saisie):
    nombre=[1,2,3,4,5,6,7,8,9,0]
    for car in saisie:
        try:
            int(car)
        except:
            return 0 
            break

    return 1 

if verif_nombre("4234123423412342342"):
    print("C'est un nombre")
else:
    print("NOP")
