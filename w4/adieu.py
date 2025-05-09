# Demande à l'utilisateur des noms, un par ligne, jusqu'à ce que l'utilisateur saisisse control-d. Supposons que l'utilisateur saisisse au moins un nom.
# Ensuite, dites adieu à ces noms, en séparant deux noms par un et, trois noms par deux virgules et un et. Exemples:# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

def main():
    names = []  # liste pour stocker les noms
    while True:
        try:
            # demander un nom
            name = input('Name: ').title().strip()
            names.append(name)  # ajouter le nom à la liste
        except EOFError:  # cela attrapera 'ctrl + d'
            break  # sortir du loop

    # préparer le message d'adieu
    print('\n')
    if len(names) == 1:
        farewell = f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        farewell = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

    print(farewell)

main()
