# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.


def main():
    # show amount
    amount = 50
    print(f"Amount Due: {amount}")

    # insert coin (quarters, dimes, nickels, pennies)
    while amount > 0:
        coin = int(input("Insert Coin [quarters/dimes/nickels/penny]: ").strip())
        if coin == 30:
            print(f"Amount Due: {amount}")
            continue
        elif coin not in [25, 10, 5, 0]:
            print("Invalid amount. Please insert a coin of denomination 25, 10, or 5.")
            continue  # use continue to repeat

        amount -= coin
        if amount > 0:
            print(f"Amount Due: {amount}")
        else:
            print(f"Change Owed: {-amount}")


main()
