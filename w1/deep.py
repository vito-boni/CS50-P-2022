# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
# Otherwise output No.

x = str(input("\nThe Answer to the Great Question…\nOf Life, the Universe and Everything…\nIs…\n").lower().strip().replace("-", "").replace(" ", ""))

match x:
    case "42" | "fortytwo":
        print ("Yes")
    case "24" | "fourty two" | "idk":
        print ("it's forty-two. lol")
    case _:
        print ("No")
