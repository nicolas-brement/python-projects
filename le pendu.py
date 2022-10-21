import random


#Question de lancement du jeu.
NiveauJoueur = input("Bonjour, à quel niveau souhaite tu jouer. Entre (d)ébutant, (i)ntermédiaire, (e)xpert ou (q) pour quitter:")

#Boucle permettant de sélectionner le niveau de jeu souhaité, le nombre de vie correspondant au niveau choisit sera affiché.
while NiveauJoueur == "q" :
        print("Vous avez quitté le jeu")
        break
if NiveauJoueur == "d":
        NbViesRestantes = 10
        print(f"Vous avez {NbViesRestantes} vies")
elif NiveauJoueur == "i":
        NbViesRestantes = 7
        print(f"Vous avez {NbViesRestantes} vies")
elif NiveauJoueur == "e" :
        NbViesRestantes = 4
        print(f"Vous avez {NbViesRestantes} vies")

        
#Ouverture du fichier "dico_france.txt" en mode lecture.
file = open("dico_france.txt", "r", encoding="ISO-8859-1")

#Procéder au tri du fichier me permettant la sélection d'un mot aléatoire.
content = file.read().split()
content = random.choice(content)

#J'affiche un message d'erreur lorsque l'utilisateur saisit plus d'une lettre.
#len me permettra de compter le nombre de lettre qu'il y a dans le mot choisi.
for guess in range(len(content)-1):
        devineLettre = str(input("Enter one letter : "))
        if (len(devineLettre)> 1):
                print("Vous ne pouvez choisir qu'un seul caractère!")
                continue

        if devineLettre in content:
                lettreSaisi = lettreSaisi + devineLettre
                print(f"Bien joué! Cette {lettreSaisi}")
        else:
                NbViesRestantes = NbViesRestantes -1
        
                
        











        

  

   

