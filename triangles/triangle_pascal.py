# ==============================================================
#  DÉFI : Triangle de Pascal
#  Auteur : Ayoub SGHIR
#  Description : Génère et affiche le triangle de Pascal
#                jusqu'à n lignes, centré dans le terminal.
# ==============================================================
#
#  Rappel mathématique :
#  ---------------------
#  Chaque élément = somme des deux éléments au-dessus de lui.
#  La 1ère et la dernière valeur de chaque ligne = toujours 1.
#
#  Exemple pour n=5 :
#          1
#         1 1
#        1 2 1
#       1 3 3 1
#      1 4 6 4 1
#
# ==============================================================


def generer_ligne(ligne_precedente):
    """
    Génère une ligne du triangle à partir de la ligne précédente.

    Principe :
    - On commence et on finit toujours par 1.
    - Les éléments du milieu = somme des deux voisins du dessus.

    Exemple :
        ligne_precedente = [1, 3, 3, 1]
        → nouvelle ligne  = [1, 4, 6, 4, 1]
                               ^  ^  ^
                             1+3 3+3 3+1
    """

    # La nouvelle ligne commence toujours par 1
    nouvelle_ligne = [1]

    # On calcule les éléments intermédiaires
    # On parcourt les paires (gauche, droite) dans la ligne précédente
    for i in range(len(ligne_precedente) - 1):
        gauche = ligne_precedente[i]
        droite = ligne_precedente[i + 1]
        nouvelle_ligne.append(gauche + droite)

    # La nouvelle ligne se termine toujours par 1
    nouvelle_ligne.append(1)

    return nouvelle_ligne


def construire_triangle(n):
    """
    Construit toutes les lignes du triangle de Pascal jusqu'à n.

    Retourne une liste de listes :
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        ...
    ]
    """

    if n <= 0:
        return []

    # Le triangle commence toujours avec la ligne [1]
    triangle = [[1]]

    # On génère chaque ligne à partir de la précédente
    for i in range(1, n):
        ligne_suivante = generer_ligne(triangle[i - 1])
        triangle.append(ligne_suivante)

    return triangle


def afficher_triangle(triangle):
    """
    Affiche le triangle centré dans le terminal.

    Stratégie d'alignement :
    - La dernière ligne est la plus large.
    - On calcule sa largeur et on centre toutes les autres par rapport à elle.

    Exemple avec n=4 :
        Dernière ligne : [1, 3, 3, 1] → affichée comme "1 3 3 1" → 7 chars
        Ligne 1        : "1"           → centrée sur 7 chars → "   1   "
        Ligne 2        : "1 1"         → centrée sur 7 chars → "  1 1  "
    """

    if not triangle:
        print("Triangle vide.")
        return

    # On calcule la largeur de la dernière ligne (la plus large)
    # join() convertit [1, 3, 3, 1] en "1 3 3 1"
    largeur_max = len(" ".join(str(x) for x in triangle[-1]))

    # On affiche chaque ligne en la centrant
    for ligne in triangle:
        # Convertit les nombres en chaîne de caractères, séparés par un espace
        ligne_str = " ".join(str(x) for x in ligne)

        # center() aligne la chaîne au milieu en ajoutant des espaces
        print(ligne_str.center(largeur_max))


def afficher_avec_separateur(n):
    """
    Version bonus : affiche le triangle avec un en-tête et un séparateur propre.
    Pratique pour rendre le rendu plus lisible dans le terminal.
    """
    print("=" * 40)
    print(f"  Triangle de Pascal — {n} lignes")
    print("=" * 40)

    triangle = construire_triangle(n)
    afficher_triangle(triangle)

    print("=" * 40)


# ==============================================================
#  POINT D'ENTRÉE
# ==============================================================

if __name__ == "__main__":

    # --- Test basique ---
    print("\n--- Test avec n=6 ---")
    afficher_avec_separateur(6)

    # --- Test avec n=10 ---
    print("\n--- Test avec n=10 ---")
    afficher_avec_separateur(10)

    # --- Interactif (optionnel) ---
    print("\n--- Mode interactif ---")
    try:
        n = int(input("Entrez le nombre de lignes : "))
        if n <= 0:
            print("Erreur : entrez un entier positif.")
        else:
            afficher_avec_separateur(n)
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide.")
