import random
min = 1
max = 6

jouer = "yes"

while jouer == "yes" or jouer == "y":
    print "Lancer les dés..."
    print "Le résultat des dés lancés est..."
    resultat1 = random.randint(min,max)
    resultat2 = random.randint(min,max)

    print resultat1
    print resultat2

    print "Le total des 2 dés lancés est..."
    print(resultat1 + resultat2)

    jouer = raw_input("Voulez-vous encore lancer les dés ?").lower()
