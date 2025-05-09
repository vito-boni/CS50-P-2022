# Invite l'utilisateur à indiquer un niveau (n). Si l'utilisateur ne saisit pas 1, 2 ou 3, le programme devrait à nouveau se le demander.
# Génère aléatoirement dix problèmes mathématiques au format 'X + Y = ', dans lesquels X et Y sont chacun un entier non négatif à 'n' chiffres.
# Pas besoin de prendre en charge des opérations autres que l'addition (+).
# Invite l'utilisateur à résoudre chacun de ces problèmes.
# Si une réponse n'est pas correcte (ou même pas un nombre), le programme doit afficher EEE et inviter à nouveau l'utilisateur, permettant à l'utilisateur jusqu'à trois essais au total pour ce problème.
# Si l'utilisateur n'a toujours pas répondu correctement après trois essais, le programme devrait afficher la bonne réponse.
# Le programme doit finalement afficher le score de l’utilisateur : le nombre de réponses correctes sur 10.

import random

def main():
    score = 1 # changé (parce que si on reduit 0 avec un '-1', on serait avoir -1, et -1 + 9 est 8. mais on peut aussi le changer avec, genre, chaque faux, -1. le score est 10)
    level = get_level()
    for _ in range(10):
        score += generate_int(level)

    print(f"Score: {score}\n")


def get_level():
    while True:
        try:
            level = int(input("Level (1-3): ").strip()) # Level (1-3)
            if level in [1, 2, 3]:
                return level
            else:
                continue

        except ValueError:
            continue


def generate_int(level):
    if level == 1:
        x, y = random.randint(0, 9), random.randint(0, 9) # corigé
    else:
        x, y = random.randint(10 ** (level - 1), 10**level - 1), random.randint(10 ** (level - 1), 10**level - 1)

    for _ in range(3):
        answer = input(f"{x} + {y} = ")
        if answer.strip() == str(x + y):
            return 1
        else:
            print("EEE")

    print(f"{x} + {y} = {x+y}")
    return -1


if __name__ == "__main__":
    main()
