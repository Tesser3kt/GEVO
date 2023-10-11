from random import randint
from collections import defaultdict

distributed = defaultdict(int)
problems = [set() for _ in range(12)]

while sum(len(p) for p in problems) < 24:
    student = randint(1, 12)
    while len(problems[student - 1]) >= 2:
        student = randint(1, 12)

    problem = randint(1, 6)
    while distributed[problem] >= 2 and problem in problems[student - 1]:
        problem = randint(1, 6)

    problems[student - 1].add(problem)
    distributed[problem] += 1

for i, p in enumerate(problems):
    print(f"Student {i + 1} has problems {p}")
