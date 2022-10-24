import random

##Le random.randint va me permettre de selectionner une réponse au hasard pour le coup de l'ordinateur.
prix = random.randint(1, 10)

score = 100

tentatives = 0

print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")

#Création d'une boucle.
while True:
    nombre = int(input())
    tentatives += 1
    if nombre < prix:
        print("Le just prix est plus haut")
    if nombre > prix:
        print("Le juste prix est plus bas")
    if nombre == prix:
        print("Félicitations, vous avez trouvé le juste prix {} en {} essais, votre score est {} !".format(prix, tentatives, int(score / tentatives)))
        break

print("Partie terminée")
