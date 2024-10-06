from datetime import datetime

def get_days_from_today(date):
    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d")
        return (datetime.today() - datetime_object).days
    except ValueError:
        return "Incorrect date format. Please, correct the format to match the following: YYYY-MM-DD"

time_delta = get_days_from_today("2025-09-05")

print(time_delta)