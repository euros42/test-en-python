#print("Hello World") Voici quelques projets débutants que j'ai essayé de faire :

#https://liora.io/10-projets-python-pour-debutants 

#1. Une alarme réveil
#Le reveil doit être à 10h pour afficher un message .#

import datetime

heure_alarme = int(input(" A quelle heure veux-tu te réveiller ? "))
min_alarme = int(input("Quelles minutes ? "))

while True :
    if heure_alarme==datetime.datetime.now().hour and min_alarme==datetime.datetime.now().minutes:
        print("Réveille toi !")

