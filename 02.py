import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min >= 1 and max <= 1000:
            chosen_numbers = random.sample(range(min, max), quantity)
            return f"Лотерейні числа: {chosen_numbers}"
        else:
            return "Wrong parameters! Please, make sure your parameters are between 1 and 1000."
    except ValueError:
        return "Please, make sure that all parameters are correct!"

res = get_numbers_ticket(1, 49, 6)

print(res)