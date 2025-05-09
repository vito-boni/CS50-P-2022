# week 2

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # if the plate has at least 2 characters and at most 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # if the plate starts with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # if there are no periods, spaces, or punctuation marks
    if not s.isalnum():
        return False

    # if numbers are only at the end and the first number is not '0'
    for i in range(2, len(s)):
        if s[i].isalpha() and any(char.isdigit() for char in s[:i]):
            return False
        if s[i] == '0' and all(char.isalpha() for char in s[:i]):
            return False

    return True

if __name__ == "__main__":
    main()


