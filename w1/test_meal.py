# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

def valid():
    while True:
        try:
            time_input = input("What time is it? ")

            # Remove colons and case-insensitive 'p.m.' or 'a.m.'
            clean_time = time_input.lower().replace(":", "").replace("p.m.", "").replace("a.m.", "")
            x = int(clean_time)

            # If 'p.m.' was in the input and the time is not noon or midnight, add 1200
            if "p.m." in time_input.lower() and x < 1200:
                x += 1200
            if 0 <= x <= 2359:
                return x
            else:
                print("Invalid time. Please enter a time between 0000 and 2359.")
        except ValueError:
            print("Invalid input. Please enter a valid time.")

x = valid()

if 700 <= x <= 800:
    print("breakfast time!")
elif 1200 <= x <= 1300:
    print("lunch time!")
elif 1800 <= x <= 1900:
    print("dinner time!")
else:
    print("bye")

"""
x, y = input("What time is it?\n").split(":")

x = int(x)
y = float(y)
y = round(y / 6)

if y == 60:
    y = 0
    x = x + 1

if 7 <= x <= 8:
    print ("breakfast time")
elif 12 <= x <= 13:
    print ("lunch time")
elif 18 <= x <= 19:
    print ("dinner time")
else:
    print("bye")

print ("\n")

"""


"""
# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
import re

def main():
    while True:
        try:
            t = input("What time is it?\n")
            if 'pm' in t or 'p.m.' in t:
                t = t.replace('pm', '').replace('p.m.', '')
                h, m = re.split(':|h', t)
                h = float(h) + 12  # add 12 to hours for pm time
            else:
                t = t.replace('am', '').replace('a.m.', '')
                h, m = re.split(':|h', t)
                h = float(h)
            m = float(m)

            if h == 24:
                h = 0
            elif m == 60:
                m = 0
                h = h + 1
            if 0 <= h <= 23 and 0 <= m <= 59:
                return (h, m)
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")

def convert(h, m):
    return h + m / 60

h, m = main()
time = convert(h, m)
time = round(time, 1)

if 7 <= time < 8:
    print (f"{time} hours, breakfast time")
elif 12 <= time < 13:
    print (f"{time} hours, lunch time")
elif 18 <= time < 19:
    print (f"{time} hours, dinner time")

"""

"""
import re

def main():
    while True:
        try:
            t = input("What time is it? ")

            if t.endswith('pm') or t.endswith('p.m.'):
                t = t.rstrip('pm').rstrip('p.m.')
                h, m = re.split(':|h', t)
                h = float(h) + 12  # add 12 to hours for pm time
            else:
                t = t.rstrip('am').rstrip('a.m.')
                h, m = re.split(':|h', t)
                h = float(h)
            m = float(m)

            if h == 24:
                h = 0
            elif m == 60:
                m = 0
                h = h + 1
            if 0 <= h <= 23 and 0 <= m <= 59:
                time_in_hours = h + m / 60
            else:
                print("Invalid")
                continue

            if 7 <= time_in_hours < 8:
                print("breakfast time")
                break
            elif 12 <= time_in_hours < 13:
                print("lunch time")
                break
            elif 18 <= time_in_hours < 19:
                print("dinner time")
                break

        except ValueError:
            print("Invalid")

if __name__ == "__main__":
    main()


"""
