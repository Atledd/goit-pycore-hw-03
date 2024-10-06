import re

def normalize_phone(phone_number):
    numbers_cleaned = re.sub(r"\D+", "", phone_number)
    normalized_numbers = re.sub(r"^\+?(38)?", "+38", numbers_cleaned)
    return normalized_numbers


raw_numbers = ["    +38(050)123-32-34", "     0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11   "]

normalized_numbers = [normalize_phone(num) for num in raw_numbers]

print(normalized_numbers)