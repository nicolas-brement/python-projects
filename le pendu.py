import random


#Question de lancement du jeu.
NiveauJoueur = input("Bonjour, à quel niveau souhaite tu jouer. Entre (d)ébutant, (i)ntermédiaire, (e)xpert ou (q) pour quitter:")
tentatives = 7
#Boucle permettant de sélectionner le niveau de jeu souhaité, le nombre de vie correspondant au niveau choisit sera affiché.
while NiveauJoueur == "q" :
        print("Vous avez quitté le jeu")
        break
if NiveauJoueur == "d":
        tentatives = 10
        print(f"Vous avez {tentatives} vies")
elif NiveauJoueur == "i":
        tentatives = 7
        print(f"Vous avez {tentatives} vies")
elif NiveauJoueur == "e" :
        tentatives = 4
        print(f"Vous avez {tentatives} vies")

        
#Ouverture du fichier "dico_france.txt" en mode lecture.
file = open("dico_france.txt", "r", encoding="ISO-8859-1")

#Procéder au tri du fichier me permettant la sélection d'un mot aléatoire.
solution = file.read().split()
solution = random.choice(solution)

affichage = ""
for l in solution:
  affichage = affichage + "_ "
lettres_trouvees = ""
print("Mot à deviner : ", affichage)

proposition = input("proposez une lettre : ")

if proposition in solution:
    lettres_trouvees = lettres_trouvees + proposition
else:
    tentatives = tentatives - 1

if proposition in solution:
    lettres_trouvees = lettres_trouvees + proposition
    print("-> Bien vu!")
else:
    tentatives = tentatives - 1
    print("-> Non cette lettre ne fait pas partie du mot. Il vous reste", tentatives, "tentatives")
                
while tentatives>0:
    print("Mot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")
    if proposition in solution:
        lettre_trouvees = lettres_trouvees + proposition
        print("-> Bien vu!")
    else:
        tentatives = tentatives - 1
        print("-> Non cette lettre ne fait pas partie du mot. Il vous reste", tentatives, "tentatives")
             
        
        affichage = ""
    for x in solution:
      if x in lettres_trouvees:
        affichage += x + " "
      else:
          affichage += "_ "
        
        

while "_" not in affichage:
        print(">>> Gagné! <<<")
        print("    * Fin de la partie *    ")
        break
        












        

  

   

