# Expects zero or two command-line arguments:
#   • Zero if the user would like to output text in a random font.
#   • Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# Resources: http://www.figlet.org/examples.html | https://pypi.org/project/pyfiglet/0.7/ | https://docs.python.org/3/library/random.html

import sys
from pyfiglet import Figlet

figlet = Figlet()

# Check if the user PROVIDED command-line arguments
if len(sys.argv) == 1:
    # If no arguments were provided, use the default font
    font = 'standard'
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    # If two arguments were provided and the first one is -f or --font, use the specified font
    font = sys.argv[2]
else:
    # Anything else, WRONG
    print("Usage: python figlet.py [-f FONT]")
    sys.exit(1)

# Set the font
figlet.setFont(font=font)

# Prompt the user for a string of text
text = input("Input: ")

# Output the text in the desired font
print(figlet.renderText(text))
