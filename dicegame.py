import random
min = 1
max = 6

jouer = "yes"

while jouer == "yes" or jouer == "y":
    print "Lancer les d�s..."
    print "Le r�sultat des d�s lanc�s est..."
    resultat1 = random.randint(min,max)
    resultat2 = random.randint(min,max)

    print resultat1
    print resultat2

    print "Le total des 2 d�s lanc�s est..."
    print(resultat1 + resultat2)

    jouer = raw_input("Voulez-vous encore lancer les d�s ?").lower()
