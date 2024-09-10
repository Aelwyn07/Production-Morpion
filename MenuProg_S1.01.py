from morpion import partie
from SauvegardeText import sav
from affichage_score import afficher

if __name__ == "__main__":
    ENT: int
    a: bool
    mor: list
    score1: list
    score2: list
    score3: list
    lst_temp: list

    ENT = 0
    a = True
    mor = [0,0]
    

    print("---------------------------------")
    print("           BIENVENUE !           ")
    print("---------------------------------")

    #Boucle tant que qui fait fonctionner le programme
    while a == True:
        print("")
        print("            Menu           ")
        print("")
        print("Que souhaitez vous faire : ")
        print(" 1 - Jouer au jeu du morpion")
        print(" 2 - Afficher les scores")
        print(" 3 - Quitter le programme")
        print("                                ")
        
        #Saisie du choix
        ENT = int(input("Veuillez saisir votre choix : "))
        while ENT < 1 or ENT > 4:
            print("Veillez saisir un nombre valide ! (entre 1 et 6)")
            ENT = int(input(""))

        #Conditions pour lancer la fonction souhaitée

        if ENT == 1:
            print(" \n---------------------------------------------------------")
            print("                 Vous jouez au Morpion !                 ")
            print("---------------------------------------------------------\n ")

            #Lancement d'une partie et actualisation des scores
            score3 = partie()
            mor[0]+=score3[0]
            mor[1]+=score3[1]

        if ENT == 2:
            afficher()

        if ENT == 3:
            print("Au revoir !")

            #Envoie des scores pour les sauvegarder
            sav(mor)

            a = False



