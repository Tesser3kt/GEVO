def is_prime(number):
    if number < 2:
        return False

    d = 2
    while d <= number:
        if number % d == 0:
            return False
        d += 1
        return True
