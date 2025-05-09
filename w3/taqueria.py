def main():
    menu = {  # it's called 'dict'
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    total = 0
    while True:
        try:
            choices = input("Enter your choice: ").strip().lower().title().split(",")

            for choice in choices:
                choice = choice.strip()

                if choice in menu:
                    total += menu[choice]
                    print(f"Total: ${total:.2f}")
                    continue
                elif choice == "Done" or choice == "That's All" or choice == "Idk":
                    print("All right. Have a nice day :)")
                    return 0
                else:
                    continue

        except EOFError:
            return 0  # use return 0 so that… idk, it's just the requirement


main()
