#Exo 1
# Demander un nombre entier à l'utilisateur
N = int(input("Entrez un nombre entier : "))

# Calculer la somme
somme = 0
for i in range(1, N + 1):
    somme += i

# Afficher le résultat
print("La somme des nombres de 1 à", N, "est", somme)

#Exo2
# Demander un nombre entier à l'utilisateur
N = int(input("Entrez un nombre entier : "))

# Afficher la table de multiplication
for i in range(1, 11):
    produit = N * i
    print(N, "x", i, "=", produit)

#Exo3
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "est pair")
    else:
        print(i, "est impair")

#Exo4
# Demander un nombre entier à l'utilisateur
N = int(input("Entrez un nombre entier : "))

# Calculer la factorielle
factorielle = 1
for i in range(1, N + 1):
    factorielle *= i

# Afficher le résultat
print("La factorielle de", N, "est", factorielle)

#Exo5
# Demander un mot à l'utilisateur
mot = input("Entrez un mot : ")

# Inverser le mot
mot_inverse = mot[::-1]

# Vérifier si le mot est un palindrome
if mot == mot_inverse:
    print(mot, "est un palindrome.")
else:
    print(mot, "n'est pas un palindrome.")
