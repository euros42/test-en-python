#print("Hello World") Ici je reteste quelques exercices effectuées en classe pendant ma premiere année de licence de mathématiques #

#Trouver les nombres pairs d'une liste de nombre:#

import math
nombres = range(51)
nombres_pairs = []

for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)

print (nombres_pairs)
