from collections import defaultdict

with open("file-2.in", "r", encoding="utf-8") as fin:
    with open("file-2.out", "w+", encoding="utf-8") as fout:
        N = int(fin.readline())
        for number in map(int, fin.readlines()):
            prime_factors = defaultdict(int)
            possible_divisors = list(range(2, int(number ** 0.5) + 1))

            # Eratosthenes' sieve
            for divisor in possible_divisors:
                if divisor == -1:
                    continue
                if divisor > number:
                    break
                while number % divisor == 0:
                    prime_factors[divisor] += 1
                    number //= divisor

                # clear all multiples of divisor
                for i in range(divisor * 2, int(number ** 0.5) + 1, divisor):
                    possible_divisors[i - 2] = -1

            factors_list = [
                f"{factor}^{power}" if power > 1 else f"{factor}"
                for factor, power in prime_factors.items()
            ]
            if factors_list:
                fout.write("*".join(factors_list) + "\n")
            else:
                fout.write(f"{number}\n")
