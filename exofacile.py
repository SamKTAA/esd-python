# Demander un nombre entier à l'utilisateur
N = int(input("Entrez un nombre entier : "))

# Calculer la somme
somme = 0
for i in range(1, N + 1):
    somme += i

# Afficher le résultat
print("La somme des nombres de 1 à", N, "est", somme)
