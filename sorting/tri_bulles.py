# ==============================================================
#  DÉFI : Tri à Bulles (Bubble Sort)
#  Niveau : Intermédiaire
#  Description : Trier une liste en comparant et en échangeant
#                les éléments adjacents jusqu'à ce que la liste
#                soit entièrement ordonnée.
#
#  Principe :
#  ----------
#  À chaque passage, on fait "remonter" le plus grand élément
#  vers la fin — comme une bulle qui remonte à la surface.
#
#  Exemple :
#  [5, 3, 8, 1, 2]
#  Passe 1 → [3, 5, 1, 2, 8]   (8 est à sa place)
#  Passe 2 → [3, 1, 2, 5, 8]   (5 est à sa place)
#  Passe 3 → [1, 2, 3, 5, 8]   (3 est à sa place)
#  Résultat → [1, 2, 3, 5, 8] ✓
#
#  Complexité :
#  - Pire cas  : O(n²)  → liste triée à l'envers
#  - Meilleur  : O(n)   → liste déjà triée (version optimisée)
#  - Mémoire   : O(1)   → tri en place, pas de liste supplémentaire
# ==============================================================


def tri_bulles(liste):
    """
    Trie une liste par ordre croissant avec le tri à bulles.
    Modifie la liste en place (ne retourne rien).

    Fonctionnement :
    - On fait n-1 passages sur la liste.
    - À chaque passage i, on compare les éléments adjacents.
    - Si l'élément gauche > élément droite → on échange.
    - Après chaque passage, le plus grand élément restant
      est positionné à sa place définitive.
    """

    n = len(liste)

    # Chaque passage place un élément de plus à sa position finale
    for i in range(n - 1):

        # Après i passages, les i derniers éléments sont déjà triés
        # On n'a donc plus besoin de les comparer → n - 1 - i
        for j in range(n - 1 - i):

            # Comparaison des deux éléments adjacents
            if liste[j] > liste[j + 1]:

                # Échange (swap) en Python : pas besoin de variable temp !
                liste[j], liste[j + 1] = liste[j + 1], liste[j]


def tri_bulles_optimise(liste):
    """
    Version optimisée : on arrête dès que la liste est triée.

    Optimisation clé :
    Si on fait un passage entier sans aucun échange,
    c'est que la liste est déjà triée → inutile de continuer.

    Gain : O(n) dans le meilleur cas (liste déjà triée).
    """

    n = len(liste)

    for i in range(n - 1):

        # On suppose qu'aucun échange ne sera nécessaire
        echange_effectue = False

        for j in range(n - 1 - i):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                echange_effectue = True  # Un échange a eu lieu

        # Si aucun échange pendant ce passage → liste triée, on arrête
        if not echange_effectue:
            print(f"  ✓ Liste triée après {i + 1} passage(s) seulement !")
            break


def tri_bulles_verbose(liste):
    """
    Version pédagogique : affiche chaque étape du tri.
    Utile pour visualiser comment l'algorithme fonctionne.
    """

    n = len(liste)
    copie = liste[:]  # On travaille sur une copie pour ne pas modifier l'original

    print(f"  Liste initiale : {copie}")

    for i in range(n - 1):
        echange_effectue = False

        for j in range(n - 1 - i):
            if copie[j] > copie[j + 1]:
                copie[j], copie[j + 1] = copie[j + 1], copie[j]
                echange_effectue = True

        print(f"  Passe {i + 1}       : {copie}")

        if not echange_effectue:
            break

    print(f"  Résultat final  : {copie}")
    return copie


# ==============================================================
#  POINT D'ENTRÉE
# ==============================================================

if __name__ == "__main__":

    # --- Test basique ---
    print("=== Tri à bulles basique ===")
    ma_liste = [64, 34, 25, 12, 22, 11, 90]
    print(f"Avant : {ma_liste}")
    tri_bulles(ma_liste)
    print(f"Après : {ma_liste}")

    # --- Test version optimisée ---
    print("\n=== Tri à bulles optimisé ===")
    liste2 = [1, 2, 3, 5, 4]  # Presque triée → peu de passages
    print(f"Avant : {liste2}")
    tri_bulles_optimise(liste2)
    print(f"Après : {liste2}")

    # --- Test version verbose ---
    print("\n=== Tri à bulles verbose (étape par étape) ===")
    liste3 = [5, 3, 8, 1, 2]
    tri_bulles_verbose(liste3)

    # --- Test liste déjà triée ---
    print("\n=== Liste déjà triée ===")
    liste4 = [1, 2, 3, 4, 5]
    tri_bulles_optimise(liste4)
    print(f"Résultat : {liste4}")

    # --- Test liste inversée (pire cas) ---
    print("\n=== Liste inversée (pire cas) ===")
    liste5 = [5, 4, 3, 2, 1]
    tri_bulles_verbose(liste5)
