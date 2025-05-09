# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

def main():
    t = input("What time is it? ").replace('h', ':').replace('.', ':').replace(' ', '')
    time_in_hours = convert(t)

    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")

def convert(t):
    h, m = map(int, t.split(":"))
    return h + m / 60

if __name__ == "__main__":
    main()
