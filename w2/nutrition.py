def main():
    # Define a dictionary with fruits as keys and calories as values
    fruits = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'sweet cherries': 100,
        'kiwifruit': 90,
        'pear': 100,
        # etc...
    }

    # Ask the user for a fruit
    fruit = input("Enter the name of a fruit: ").lower().strip()

    # Check if the fruit is in the dictionary
    if fruit in fruits:
        print(f"{fruits[fruit]}")


main()
