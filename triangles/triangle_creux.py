# ==============================================================
#  DÉFI : Triangle Creux
#  Auteur : Ayoub SGHIR
#  Description : Affiche un triangle rectangle dont seuls
#                les bords sont remplis d'étoiles.
#
#  Exemple pour n=6 :
#  *
#  **
#  *  *
#  *   *
#  *    *
#  *******
# ==============================================================


def triangle_creux(n):
    """
    Affiche un triangle creux de n lignes.

    Règles d'affichage :
    - Ligne 1       → une seule étoile (sommet)
    - Ligne 2       → deux étoiles (encore plein, trop petit pour être creux)
    - Lignes 3 à n-1 → étoile à gauche + espaces + étoile à droite (creux)
    - Dernière ligne → toute remplie d'étoiles (base)
    """

    for i in range(1, n + 1):

        if i == 1:
            # Sommet du triangle : une seule étoile
            print("*")

        elif i == n:
            # Base du triangle : ligne pleine
            # i étoiles collées les unes aux autres
            print("*" * i)

        elif i == 2:
            # Deuxième ligne : trop petite pour être creuse, on met 2 étoiles
            print("**")

        else:
            # Lignes du milieu : creux
            # Structure : * + espaces + *
            # Nombre d'espaces = i - 2
            # (i colonnes au total, moins les 2 étoiles aux bords)
            espaces = " " * (i - 2)
            print("*" + espaces + "*")


def triangle_creux_centre(n):
    """
    Version bonus : triangle creux centré dans le terminal.
    La base fait (2*n - 1) caractères, les autres lignes sont centrées.
    """
    largeur = 2 * n - 1

    for i in range(1, n + 1):
        if i == 1:
            ligne = "*"
        elif i == n:
            ligne = "*" * (2 * i - 1)
        else:
            espaces_internes = " " * (2 * i - 3)
            ligne = "*" + espaces_internes + "*"

        print(ligne.center(largeur))


# ==============================================================
#  POINT D'ENTRÉE
# ==============================================================

if __name__ == "__main__":

    print("=== Triangle creux (n=6) ===")
    triangle_creux(6)

    print("\n=== Triangle creux (n=8) ===")
    triangle_creux(8)

    print("\n=== Triangle creux centré (n=6) ===")
    triangle_creux_centre(6)
