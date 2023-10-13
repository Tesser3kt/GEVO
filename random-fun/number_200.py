x = int(input("Enter a number: "))

digits = []
while x != 0:
    digits.append(x % 200)
    x //= 200

powers = [str(digits[i]) + " * 200^" + str(i) for i in range(len(digits))]
print(" + ".join(powers))
