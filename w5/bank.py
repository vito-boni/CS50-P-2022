# week 1: #bank.py

# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
# g = greetings

def some_function(func):
    def wrapper(*args, **kwargs):
        print("Entered some_function")
        result = func(*args, **kwargs)
        print("Exiting some_function")
        return result
    return wrapper

@some_function
def main():
    g = str(input("Check: ").lower().strip().replace(",", ""))
    print(value(g))  # print the result of value(g)
    return

def value(g):
    first_word = g.split()[0]

    if first_word == "hello":
        return "$0"
    elif first_word[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()

"""
def main():
    g = str(input("Check: ").lower().strip().replace(",", ""))
    print(value(g))  # print the result of value(g)
    return

def value(g):
    first_word = g.split()[0]

    if first_word == "hello":
        print("$0")
    elif first_word[0] == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
"""
