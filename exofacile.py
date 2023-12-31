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

#Exo 1 chapitre 4 : Manipulation de Listes
Créez une liste de nombres, ajoutez-y des éléments, puis triez-la.

# Créer une liste de nombres
ma_liste = [5, 3, 1, 4, 2]

# Ajouter des éléments
ma_liste.append(6)
ma_liste.append(7)

# Trier la liste
ma_liste.sort()

# Afficher la liste triée
print(ma_liste)

#Exo 2 chapitre 4 : Créez un dictionnaire représentant une personne, incluant des informations telles que le nom, l'âge, et l'adresse.

# Créer un dictionnaire représentant une personne
personne = {
    "nom": "Dupont",
    "age": 30,
    "adresse": "123 rue de la Paix"
}

# Ajouter des informations
personne["telephone"] = "0618293021"

# Modifier des informations
personne["adresse"] = "456 avenue de la Liberté"

# Afficher des informations spécifiques
print("Nom:", personne["nom"])

# Afficher le dictionnaire complet
print(personne)

#Exo 3 chapitre 4 : Définissez deux ensembles et effectuez des opérations comme l'union et l'intersection.

# Définir deux ensembles
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

# Union des ensembles
union = ensemble1 | ensemble2

# Intersection des ensembles
intersection = ensemble1 & ensemble2

# Afficher les résultats
print("Union:", union)
print("Intersection:", intersection)

#Exo : Gestionnaire de contacts : écrivez un programme qui stocke les noms et numéro de téléphone des contacts dans un dictionnaire et permet à l'utilisateur d'ajouter, supprimer ou rechercher un contact 

contacts = {}

def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    numero = input("Entrez le numéro de téléphone : ")
    contacts[nom] = numero
    print("Contact ajouté.")

def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer : ")
    if nom in contacts:
        del contacts[nom]
        print("Contact supprimé.")
    else:
        print("Contact non trouvé.")

def rechercher_contact():
    nom = input("Entrez le nom du contact à rechercher : ")
    if nom in contacts:
        print("Numéro de téléphone :", contacts[nom])
    else:
        print("Contact non trouvé.")

while True:
    choix = input("Choisissez une option: ajouter, supprimer, rechercher, quitter : ").lower()
    if choix == 'ajouter':
        ajouter_contact()
    elif choix == 'supprimer':
        supprimer_contact()
    elif choix == 'rechercher':
        rechercher_contact()
    elif choix == 'quitter':
        print("Programme terminé.")
        break
    else:
        print("Option non valide.")

#Exo : Convertisseur Température : créez une fonction qui convertit les températeurs entre Celsius et Fahrenheit.

def convertir_temperature(temp, unite):
    if unite == "C":
        return (temp * 9/5) + 32
    elif unite == "F":
        return (temp - 32) * 5/9
    else:
        return "Unité non reconnue."

# Exemple de conversion
temp_celsius = 30
temp_fahrenheit = convertir_temperature(temp_celsius, "C")
print(f"{temp_celsius}C est équivalent à {temp_fahrenheit}F")

temp_fahrenheit = 86
temp_celsius = convertir_temperature(temp_fahrenheit, "F")
print(f"{temp_fahrenheit}F est équivalent à {temp_celsius}C")

#Exo : Calculateur d'IMC : écrivez une fonction qui calcule l'Indice de Masse Corporelle (IMC) à partir de la taille et du poids données.

def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    return imc

# Exemple d'utilisation
poids = 70 # en kilogrammes
taille = 1.75 # en mètres

imc = calculer_imc(poids, taille)
print(f"L'IMC calculé est : {imc:.2f}")

#Exo : Tri de liste : écrivez une fonction qui prend une liste de nombres et retourne une liste triée sans utiliser la méthode .sort()

def tri_par_insertion(liste):
    liste_triee = liste.copy()
    for i in range(1, len(liste_triee)):
        element_a_inserer = liste_triee[i]
        j = i - 1
        while j >= 0 and liste_triee[j] > element_a_inserer:
            liste_triee[j + 1] = liste_triee[j]
            j -= 1
        liste_triee[j + 1] = element_a_inserer
    return liste_triee

ma_liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
liste_triee = tri_par_insertion(ma_liste)
print("Liste originale:", ma_liste)
print("Liste triée:", liste_triee)

#Exo : tri à bulle 

def tri_a_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri_a_bulles(ma_liste)
print("Liste triée :")
print(ma_liste)
