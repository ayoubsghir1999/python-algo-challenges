# ==============================================================
#  DÉFI : Palindrome
#  Niveau : Débutant / Intermédiaire
#  Description : Vérifier si un mot, une phrase ou un nombre
#                est un palindrome — c'est-à-dire qu'il se lit
#                pareil dans les deux sens.
#
#  Exemples :
#  - "radar"         → palindrome ✓
#  - "Kayak"         → palindrome ✓ (insensible à la casse)
#  - "Engage le jeu que je le gagne"  → palindrome ✓ (sans espaces)
#  - "bonjour"       → pas un palindrome ✗
#  - 121             → palindrome (nombre) ✓
#  - 123             → pas un palindrome ✗
# ==============================================================


# ==============================================================
#  MÉTHODE 1 : Avec le slicing Python  [::-1]
#  La plus courte et pythonique
# ==============================================================

def est_palindrome_simple(chaine):
    """
    Vérifie si une chaîne est un palindrome avec le slicing.

    chaine[::-1] retourne la chaîne à l'envers.
    Ex : "radar"[::-1] → "radar"

    Sensible à la casse et aux espaces :
    "Radar" → "radaR" ≠ "Radar" → False (sans nettoyage)
    """
    return chaine == chaine[::-1]


# ==============================================================
#  MÉTHODE 2 : Robuste — insensible à la casse et aux espaces
# ==============================================================

def nettoyer(chaine):
    """
    Prépare la chaîne pour la comparaison :
    - Convertit en minuscules (insensible à la casse)
    - Supprime les espaces et la ponctuation
    - Garde uniquement les lettres et chiffres

    Exemple :
    "Engage le jeu que je le gagne !"
    → "engagelejeugejelegagne"
    """
    return "".join(
        caractere.lower()               # minuscule
        for caractere in chaine
        if caractere.isalnum()          # garde lettres et chiffres uniquement
    )


def est_palindrome(chaine):
    """
    Vérifie si une chaîne est un palindrome de façon robuste.
    Insensible à la casse, aux espaces et à la ponctuation.
    """
    chaine_nettoyee = nettoyer(chaine)
    return chaine_nettoyee == chaine_nettoyee[::-1]


# ==============================================================
#  MÉTHODE 3 : Avec deux pointeurs (Two Pointers)
#  Technique classique souvent demandée en entretien tech
# ==============================================================

def est_palindrome_deux_pointeurs(chaine):
    """
    Vérifie si une chaîne est un palindrome avec deux pointeurs.

    Principe :
    - Un pointeur `gauche` part du début  → avance vers la droite
    - Un pointeur `droite` part de la fin → recule vers la gauche
    - On compare les deux caractères à chaque étape
    - Si on trouve une différence → pas un palindrome
    - Si les pointeurs se croisent sans différence → palindrome !

    Avantage : on s'arrête dès la première différence trouvée.
    C'est plus efficace que de retourner toute la chaîne.

    Exemple avec "radar" :
    g=0 d=4 → 'r' == 'r' ✓
    g=1 d=3 → 'a' == 'a' ✓
    g=2 d=2 → les pointeurs se croisent → STOP → palindrome !
    """

    chaine = nettoyer(chaine)  # On nettoie d'abord

    gauche = 0                  # Pointeur gauche : commence au début
    droite = len(chaine) - 1    # Pointeur droite : commence à la fin

    while gauche < droite:

        if chaine[gauche] != chaine[droite]:
            # Les caractères sont différents → pas un palindrome
            return False

        # On rapproche les deux pointeurs
        gauche += 1
        droite -= 1

    # Les pointeurs se sont croisés sans erreur → c'est un palindrome
    return True


# ==============================================================
#  BONUS : Palindrome pour les nombres entiers
# ==============================================================

def est_palindrome_nombre(n):
    """
    Vérifie si un entier est un palindrome.

    Astuce : on convertit le nombre en chaîne et on compare.
    Les négatifs ne peuvent pas être des palindromes (à cause du '-').

    Exemples :
    121  → "121"  → "121"[::-1] = "121"  → ✓
    -121 → négatif → ✗ directement
    10   → "10"   → "01"        ≠ "10"   → ✗
    """

    if n < 0:
        return False  # Un nombre négatif n'est jamais un palindrome

    chaine = str(n)
    return chaine == chaine[::-1]


def afficher_resultat(valeur, resultat):
    """Affiche le résultat de façon lisible."""
    symbole = "✓ Palindrome" if resultat else "✗ Pas un palindrome"
    print(f"  '{valeur}' → {symbole}")


# ==============================================================
#  POINT D'ENTRÉE
# ==============================================================

if __name__ == "__main__":

    # --- Test méthode simple ---
    print("=== Méthode simple (slicing) ===")
    afficher_resultat("radar",   est_palindrome_simple("radar"))
    afficher_resultat("bonjour", est_palindrome_simple("bonjour"))
    afficher_resultat("Radar",   est_palindrome_simple("Radar"))   # Casse sensible → False

    # --- Test méthode robuste ---
    print("\n=== Méthode robuste (insensible à la casse et espaces) ===")
    afficher_resultat("Kayak",                          est_palindrome("Kayak"))
    afficher_resultat("Engage le jeu que je le gagne",  est_palindrome("Engage le jeu que je le gagne"))
    afficher_resultat("A man a plan a canal Panama",    est_palindrome("A man a plan a canal Panama"))
    afficher_resultat("Python",                         est_palindrome("Python"))

    # --- Test deux pointeurs ---
    print("\n=== Méthode deux pointeurs ===")
    afficher_resultat("laval",   est_palindrome_deux_pointeurs("laval"))
    afficher_resultat("level",   est_palindrome_deux_pointeurs("level"))
    afficher_resultat("bonjour", est_palindrome_deux_pointeurs("bonjour"))

    # --- Test nombres ---
    print("\n=== Palindromes numériques ===")
    for nombre in [121, 1221, -121, 10, 0, 99, 100]:
        symbole = "✓" if est_palindrome_nombre(nombre) else "✗"
        print(f"  {nombre} → {symbole}")
