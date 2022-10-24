import random
#Saisi du nom du joueur.
nom = input("Veuillez saisir votre nom: ")

#Pour stocker les victoires du joueur et de l'ordinateur.
user_victoires = 0
pc_victoires = 0
nuls = 0

#Création d'une boucle proposant au joueur de choisir soin coup ou de quitter de le jeu.
while True :
    coupJoueur = input("Entrez votre coup: (p)ierre, (f)euille, (c)iseaux ou (q)uitter : ")
    if coupJoueur =="q" :
        print("Vous avez quitté le jeu")
        break #Permet de quitter la boucle si le joueur décide de quitter.
    if coupJoueur != "p" and coupJoueur != "f" and coupJoueur !="c" :
        continue

#Programmation des différents scénarios du jeu pour définir le gagnants.
    if coupJoueur == "p" :
        print("PIERRE contre ...",end="  ")
    elif coupJoueur == "f" :
            print("FEUILLE contre ...",end='  ')
    else:
                print("CISEAUX contre ...",end='  ')

#Le random.randint va me permettre de selectionner une réponse au hasard pour le coup de l'ordinateur.
    randomNombre = random.randint (1,3)
    if randomNombre == 1 :
        coupPC = "p"
        print("PIERRE")
    elif randomNombre == 2 :
        coupPC = "f"
        print("FEUILLE")
    else:
        coupPC = "c"
        print("CISEAUX")

    if coupJoueur == coupPC :
        print("Match nul!")
        nuls = nuls + 1
    elif coupJoueur =="p" and coupPC =="c" :
        print("Vous avez gagné!")
        user_victoires = user_victoires + 1
    elif coupJoueur =="f" and coupPC =="p" :
        print("Vous avez gagné!")
        user_victoires = user_victoires + 1
    elif coupJoueur =="c" and coupPC =="f" :
        print("Vous avez gagné!")
        user_victoires = user_victoires + 1
    elif coupJoueur =="p" and coupPC =="f" :
        print("Vous avez perdu! ")
        pc_victoires = pc_victoires +1
    elif coupJoueur =="f" and coupPC =="c" :
     print("Vous avez perdu! ")
     pc_victoires = pc_victoires +1
    elif coupJoueur =="c" and coupPC =="p" :
        print("Vous avez perdu! ")
        pc_victoires = pc_victoires +1






