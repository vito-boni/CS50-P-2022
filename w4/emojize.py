import re

def main():

    # emoji dict
    emojis = {
        ':thumbsup:': '👍',
        ':1st_place_medal:': '🥇',
        ':moneybag:': '💰',
        ':smile_cat:': '😸',
        ':earth_asia:': '🌏',
        ':candy:': '🍬',
        ':ice_cream:': '🍨',
    }

    # get input
    user_input = input().strip()

    # for each emoji in the dictionary
    for emoji in emojis:
        user_input = user_input.replace(emoji, emojis[emoji])   # replace the emoji with its corresponding value

    # print the result
    print(user_input)

main()
