# implement a program that prompts the user for a date, anno Domini, in month-day-year order
# formatted like 9/8/1636 or September 8, 1636
# reject 8 september, 2000
# reject if the date > 31

import datetime


def main():
    while True:
        date = input("Insert the date: ").strip()

        # date is in 'mm/dd/yyyy' format
        try:
            d = datetime.datetime.strptime(
                date, "%m/%d/%Y"
            )  # parse the date in the format 'mm/dd/yyyy'
            print(
                f"{d.year}-{d.month:02}-{d.day:02}"
            )  # use f-string formatting to print month and day with leading zeros
            break
        except ValueError:
            pass

        # Check if the date is in 'Month dd, yyyy' format
        try:
            d = datetime.datetime.strptime(
                date, "%B %d, %Y"
            )  # parse the date in the format 'monthname dd, yyyy'
            print(
                f"{d.year}-{d.month:02}-{d.day:02}"
            )  # use f-string formatting to print month and day with leading zeros
            break

        except ValueError:
            pass

        print("Desolé, mais ca marche pas. À plus !")


main()
