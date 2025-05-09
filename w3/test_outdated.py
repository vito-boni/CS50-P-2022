# implement a program that prompts the user for a date, anno Domini, in month-day-year order
# formatted like 9/8/1636 or September 8, 1636
import datetime

months = {
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
}

# def a dictionary to map month names to numbers
month_to_num = {name: num for num, name in enumerate(months, start=1)} #  allows you to loop over a list (or other iterable object) and have an automatic counter

def conv_date(d_str):
    d_str = d_str.replace('/', '-').replace(' ', '-').replace(',', '') # j'ai oublié que je dois remplacer espace à '-'

    try:
        date = datetime.datetime.strptime(d_str, '%m-%d-%Y')  # parse the date in the format 'mm-dd-yyyy'
        return date.strftime('%Y-%m-%d')
    except ValueError:
        pass

    for month in months:
        try:
            date = datetime.datetime.strptime(d_str, f'{month}-%d-%Y')  # parse the date in the format 'monthname-dd-yyyy'
            return date.strftime('%Y-%m-%d')
        except ValueError:
            pass

    # If all parsing attempts fail = return None
    return None

while True:
    d_str = input('Insert the Date ("mm dd, yyy" or "mm-dd-yyyy"): ').title()
    if d_str.isdigit():

    converted_date = conv_date(d_str)
    if converted_date is not None:
        print(f'{converted_date}')
        break
    else:
        continue
