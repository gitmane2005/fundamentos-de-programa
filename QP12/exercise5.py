import random
def cows_bulls(seed_value):
    random.seed(seed_value)
    correct_number = random.randint(0, 9999)

    def calculate_score(guess):
        correct_str = str(correct_number)
        guess_str = str(guess)

        cows = sum(c == g for c, g in zip(correct_str, guess_str))
        bulls = sum(c in guess_str and c != g for c, g in zip(correct_str, guess_str))

        return (cows, bulls)

    return calculate_score
print(cows_bulls(60712)(8838))