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

#Exo6 
N = int(input("Entrez un nombre impair pour la taille du carré magique : "))

# Vérification si N est impair
if N % 2 == 0:
    print("Le nombre doit être impair.")
    exit()

# Création d'une matrice N x N initialisée à 0
carre = [[0]*N for _ in range(N)]

# Position de départ
i = N // 2
j = N - 1

# Placement des nombres
for num in range(1, N*N + 1):
    if i == -1 and j == N: # Cas particulier
        j = N - 2
        i = 0
    else:
        if j == N:
            j = 0
        if i < 0:
            i = N - 1
            
    if carre[i][j]: # Cellule déjà remplie
        j -= 2
        i += 1
        continue
    else:
        carre[i][j] = num
        i -= 1
        j += 1

# Affichage du carré magique
for i in range(N):
    for j in range(N):
        print(carre[i][j], end=' ')
    print()
