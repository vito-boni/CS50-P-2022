# Attendez que l'utilisateur spécifique comme argument de ligne de commande le nombre de Bitcoins, n, qu'il souhaite acheter.
# Si cet argument ne peut pas être converti en float, le programme doit se terminer via sys.exit avec un message d'erreur.
# Ressources : https://api.coindesk.com/v1/bpi/currentprice.json | docs.python.org/3/library/sys.html#sys.argv


import requests
import sys


def main():
    # valider
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_bitcoins>")
        sys.exit(1)

    # convert l'argument au float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: The number of Bitcoins must be a number.")
        sys.exit(1)

    # fetch
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        print("Error: Could not fetch the current price of Bitcoin.")
        sys.exit(1)

    data = response.json()
    current_price = float(data["bpi"]["USD"]["rate"].replace(",", ""))

    amount = num_bitcoins * current_price

    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
