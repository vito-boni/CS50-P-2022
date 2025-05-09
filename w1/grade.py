
def valid_score():
    while True:
        try:
            s = int(input("Your score here: "))
            if 0 <= s <= 100:
                return s
            else:
                print ("invalid")
        except ValueError:
            print ("invalid")

s = valid_score()

if s == 100:
    print("A+")
elif s >= 90:
    print("A")
elif s >= 80:
    print ("B")
elif s >= 70:
    print ("C")
elif s >= 60:
    print ("D")
else:
    print ("F")
