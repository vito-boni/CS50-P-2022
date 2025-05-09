from CS50p.w2.plates import main

def test_num():
    assert main("AA22A") == "Invalid"
    assert main("AA022") == "Invalid"

def test_letters():
    assert main("A2222") == "Invalid"
    assert main("AAAA2345") == "Invalid"
    assert main(". ,") == "Invalid"

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
