# week 2
# implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
import re

def shorten():
    i = str(input("Input: ").strip())
    i = re.sub(
        r"[aæåäáâaàiïíîìuüúûùeëéêèoœöóôòAÆÅÄÁÂAÀIÏÍÎÌUÜÚÛÙEËÉÊÈOŒÖÓÔÒ]", "", i
    )  # literally no vowels are allowed!
    print(i)
    return

if __name__ == "__main__":
    shorten()
