# week 3

def main():
    while True:
        try:
            x, y = map(
                int, input("Fraction: ").strip().split("/")
            )  # the 'map()' is to converts each item in the list to an integer
            f = round(
                (x / y) * 100
            )  # 'int()' can't be used in 'x, y = …' situation; also we want it simple. round it.

            if f > 100:
                print("too much for your tank!")
                continue

            get_f(f)  # don't forget to call this :)
            break  # don't forget to 'break' the loop :)

        except (ValueError, ZeroDivisionError):
            continue


def get_f(f):
    if f <= 2:
        print("E")
    elif f >= 98:
        print("F")
    else:
        print(f"{f}%")


main()
