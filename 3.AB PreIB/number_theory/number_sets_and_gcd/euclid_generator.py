from random import randint


def gcd_with_steps(a: int, b: int) -> tuple[int, int]:
    steps = 0
    if a < b:
        a, b = b, a

    while b != 0:
        steps += 1
        a, b = b, a % b

    return a, steps


a = randint(100, 5000)
b = randint(100, 5000)

gcd, steps = gcd_with_steps(a, b)
while (gcd < 10) or not (4 <= steps <= 6):
    a = randint(100, 5000)
    b = randint(100, 5000)

    gcd, steps = gcd_with_steps(a, b)

print(a, b, gcd, steps)
