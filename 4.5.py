# -*- Coding:latin-1 -*-
mins=60
hours=3600
day=86400
#month=2678400
month=2628000#Moyenne de 365/12 pour avoir les 31/30 sans prise de tête
year=31536000
nbseconds=118260000#3.75 years

nbyear=(nbseconds-(nbseconds%year))/year
nbseconds=nbseconds%year

nbmonth=(nbseconds-(nbseconds%month))/month
nbseconds=nbseconds%month

nbday=(nbseconds-(nbseconds%day))/day
nbseconds=nbseconds%day

nbhours=(nbseconds-(nbseconds%hours))/hours
nbseconds=nbseconds%hours

nbmins=(nbseconds-(nbseconds%mins))/mins
nbseconds=nbseconds%mins

print(nbyear, " années, ", nbmonth, " mois, ", nbday, " jours, ", nbhours, " heures ", nbmins, " minutes, ", nbseconds, " secondes.")
