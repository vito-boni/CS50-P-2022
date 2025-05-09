# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# default = application/octet-stream
import re
file = input("Input the File Name: ").lower().strip()
file = re.sub(r"[ ,]", "", file)

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg")
    print("image/jpeg")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"): # problems…
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

