# ==============================================================
#  DÉFI : Suite de Fibonacci
#  Niveau : Intermédiaire
#  Description : Générer les termes de la suite de Fibonacci
#                de trois façons différentes : itérative,
#                récursive, et avec mémoïsation.
#
#  Définition mathématique :
#  -------------------------
#  F(0) = 0
#  F(1) = 1
#  F(n) = F(n-1) + F(n-2)  pour n >= 2
#
#  Les premiers termes :
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
#  Applications réelles :
#  - Spirale dorée en nature (fleurs, coquillages)
#  - Algorithmes de recherche (Fibonacci search)
#  - Cryptographie et mathématiques
# ==============================================================


# ==============================================================
#  MÉTHODE 1 : Itérative
#  La plus efficace — O(n) en temps, O(1) en mémoire
# ==============================================================

def fibonacci_iteratif(n):
    """
    Calcule le n-ième terme de Fibonacci de façon itérative.

    On garde uniquement les deux derniers termes en mémoire
    et on avance pas à pas — pas besoin de stocker toute la suite.

    Complexité :
    - Temps   : O(n)  → un seul passage
    - Mémoire : O(1)  → seulement 2 variables
    """

    if n < 0:
        raise ValueError("n doit être un entier positif ou nul.")

    if n == 0:
        return 0
    if n == 1:
        return 1

    # On initialise les deux premiers termes
    precedent = 0   # F(0)
    actuel    = 1   # F(1)

    # On calcule F(2), F(3), ..., F(n) en avançant
    for _ in range(2, n + 1):
        suivant   = precedent + actuel  # F(i) = F(i-1) + F(i-2)
        precedent = actuel              # On décale d'un cran
        actuel    = suivant

    return actuel


def suite_fibonacci(n):
    """
    Retourne la liste des n premiers termes de Fibonacci.
    Utile pour afficher toute la suite jusqu'au rang n.
    """

    if n <= 0:
        return []

    suite = [0, 1]

    for i in range(2, n):
        # Chaque terme = somme des deux précédents
        suite.append(suite[i - 1] + suite[i - 2])

    return suite[:n]  # On s'assure de retourner exactement n termes


# ==============================================================
#  MÉTHODE 2 : Récursive (naive)
#  Élégante mais inefficace — O(2^n) en temps
# ==============================================================

def fibonacci_recursif(n):
    """
    Calcule le n-ième terme de Fibonacci par récursion.

    Très lisible, mais dangereux pour les grands n :
    fibonacci_recursif(40) recalcule les mêmes valeurs
    des millions de fois !

    Complexité :
    - Temps   : O(2^n) → arbre de récursion exponentiel
    - Mémoire : O(n)   → profondeur de la pile d'appels
    """

    # Cas de base : conditions d'arrêt de la récursion
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Cas récursif : on décompose le problème en sous-problèmes
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)


# ==============================================================
#  MÉTHODE 3 : Mémoïsation (récursion intelligente)
#  Combine la lisibilité de la récursion + l'efficacité de l'itératif
#  Complexité : O(n) en temps et en mémoire
# ==============================================================

def fibonacci_memo(n, memo={}):
    """
    Version récursive avec mémoïsation.

    On stocke les résultats déjà calculés dans un dictionnaire (memo).
    Avant chaque calcul, on vérifie si la valeur est déjà connue.
    Si oui → on la retourne directement sans recalculer.

    Complexité :
    - Temps   : O(n) → chaque valeur calculée une seule fois
    - Mémoire : O(n) → le dictionnaire grandit jusqu'à n entrées
    """

    # Cas de base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Si déjà calculé, on retourne directement le résultat mémorisé
    if n in memo:
        return memo[n]

    # Sinon, on calcule et on mémorise avant de retourner
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# ==============================================================
#  POINT D'ENTRÉE
# ==============================================================

if __name__ == "__main__":

    # --- Afficher les 15 premiers termes ---
    print("=== Suite de Fibonacci (15 premiers termes) ===")
    suite = suite_fibonacci(15)
    print(" → ".join(str(x) for x in suite))

    # --- Comparer les 3 méthodes ---
    print("\n=== Comparaison des 3 méthodes pour n=10 ===")
    n = 10
    print(f"Itératif   : F({n}) = {fibonacci_iteratif(n)}")
    print(f"Récursif   : F({n}) = {fibonacci_recursif(n)}")
    print(f"Mémoïsation: F({n}) = {fibonacci_memo(n)}")

    # --- Test de performance sur un grand n ---
    print("\n=== Grand n (n=50) — itératif vs mémoïsation ===")
    print(f"Itératif    : F(50) = {fibonacci_iteratif(50)}")
    print(f"Mémoïsation : F(50) = {fibonacci_memo(50)}")
    print("(Ne pas essayer fibonacci_recursif(50) → trop lent !)")

    # --- Vérification rapide ---
    print("\n=== Vérification : F(n) = F(n-1) + F(n-2) ===")
    for i in range(2, 8):
        f_n   = fibonacci_iteratif(i)
        f_n1  = fibonacci_iteratif(i - 1)
        f_n2  = fibonacci_iteratif(i - 2)
        check = "✓" if f_n == f_n1 + f_n2 else "✗"
        print(f"  F({i})={f_n} = F({i-1})={f_n1} + F({i-2})={f_n2}  {check}")
