import datetime as dt

today = dt.date.today()


def ask_for_date():
    user_given_date = input("Input dates ONLY in DD/MM/YYYY: ")
    year = user_given_date[6:10]
    month = user_given_date[3:5]
    day = user_given_date[0:2]

    return int(year), int(month), int(day)


def format_date(year, month, day):
    target_date = dt.date(year, month, day)
    return target_date


y, m, d = ask_for_date()
target_date = format_date(y, m, d)

difference = today - target_date

years = difference.days // 365
months = (difference.days % 365) // 31

print(f"{years} years and {months} months.")
