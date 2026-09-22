# exercices 10
import random


nombre_secret = random.randint(1, 100)
essais = 0

print("Bienvenue au jeu de devinette !")
print("Devinez le nombre entre 1 et 100.")

while True:
    try:
        choix = int(input("Votre nombre : "))
        essais += 1
        
        if choix < nombre_secret:
            print("C'est plus grand !")
        elif choix > nombre_secret:
            print("C'est plus petit !")
        else:
            user = input(f"Bravo ! Trouvé en {essais} essais.\nVoulez-vous rejouez ? (O/N) : ")
            if user == "O":
                essais = 0
                nombre_secret = random.randint(1, 100)
            elif user == "N":
                break
            else:
                ...
    except ValueError:
        print("Veuillez entrer un nombre valide.")