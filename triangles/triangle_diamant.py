# ==============================================================
#  DÉFI : Triangle Diamant (Losange)
#  Niveau : Difficile
#  Description : Affiche un losange parfaitement symétrique
#                fait d'étoiles, centré dans le terminal.
#
#  Exemple pour n=5 (n = demi-hauteur) :
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
#
#  Astuce : un losange = triangle normal + triangle inversé
#           sans répéter la ligne du milieu.
# ==============================================================


def moitie_haute(n, largeur):
    """
    Génère la partie haute du losange (triangle croissant).
    Ligne i contient (2*i - 1) étoiles, centrées sur `largeur` chars.

    Exemple pour n=5 :
        i=1 → 1 étoile  →  "    *    "
        i=2 → 3 étoiles →  "   ***   "
        i=3 → 5 étoiles →  "  *****  "
        ...
    """
    for i in range(1, n + 1):
        # Nombre d'étoiles : toujours impair (1, 3, 5, 7...)
        nb_etoiles = 2 * i - 1
        ligne = "*" * nb_etoiles
        print(ligne.center(largeur))


def moitie_basse(n, largeur):
    """
    Génère la partie basse du losange (triangle décroissant).
    On part de n-1 pour ne pas répéter la ligne du milieu.

    Exemple pour n=5 :
        i=4 → 7 étoiles →  "   *******   "
        i=3 → 5 étoiles →  "    *****    "
        ...
        i=1 → 1 étoile  →  "      *      "
    """
    for i in range(n - 1, 0, -1):
        nb_etoiles = 2 * i - 1
        ligne = "*" * nb_etoiles
        print(ligne.center(largeur))


def diamant(n):
    """
    Affiche un losange complet de hauteur (2*n - 1).

    Paramètre :
        n : demi-hauteur du losange (nombre de lignes de la partie haute)

    La largeur totale = 2*n - 1 (ligne la plus large, au milieu).
    """

    if n <= 0:
        print("Erreur : n doit être un entier positif.")
        return

    # Largeur de la ligne la plus large (celle du milieu)
    largeur = 2 * n - 1

    print(f"=== Diamant (n={n}) ===")

    # Partie haute : du sommet jusqu'à la ligne la plus large
    moitie_haute(n, largeur)

    # Partie basse : de la ligne en dessous du milieu jusqu'en bas
    moitie_basse(n, largeur)


def diamant_creux(n):
    """
    Version bonus : losange creux (seuls les bords sont en étoiles).

    Règles :
    - Ligne du sommet et du bas : 1 étoile
    - Ligne du milieu           : toute remplie
    - Autres lignes             : étoile gauche + espaces + étoile droite
    """

    largeur = 2 * n - 1

    print(f"=== Diamant creux (n={n}) ===")

    # Partie haute
    for i in range(1, n + 1):
        nb_etoiles = 2 * i - 1
        if nb_etoiles == 1:
            # Sommet : une seule étoile
            ligne = "*"
        elif i == n:
            # Milieu : ligne pleine
            ligne = "*" * nb_etoiles
        else:
            # Lignes creuses : bords seulement
            espaces = " " * (nb_etoiles - 2)
            ligne = "*" + espaces + "*"
        print(ligne.center(largeur))

    # Partie basse (symétrique, sans répéter le milieu)
    for i in range(n - 1, 0, -1):
        nb_etoiles = 2 * i - 1
        if nb_etoiles == 1:
            ligne = "*"
        else:
            espaces = " " * (nb_etoiles - 2)
            ligne = "*" + espaces + "*"
        print(ligne.center(largeur))


# ==============================================================
#  POINT D'ENTRÉE
# ==============================================================

if __name__ == "__main__":

    diamant(5)
    print()
    diamant(7)
    print()
    diamant_creux(5)
