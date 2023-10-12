from random import randint
from collections import defaultdict

STUDENTS = 12
PROBLEMS = 6
PROBLEMS_PER_STUDENT = 2
MAX_DISTRIB = 4

distributed = defaultdict(int)
problems = [set() for _ in range(STUDENTS)]

while sum(len(p) for p in problems) < PROBLEMS_PER_STUDENT * STUDENTS:
    student = randint(1, STUDENTS)
    while len(problems[student - 1]) >= PROBLEMS_PER_STUDENT:
        student = randint(1, STUDENTS)

    problem = list(sorted(range(1, PROBLEMS + 1),
                   key=lambda x: distributed[x]))[0]
    while (distributed[problem] >= MAX_DISTRIB
           or problem in problems[student - 1]):
        problem = randint(1, PROBLEMS)

    problems[student - 1].add(problem)
    distributed[problem] += 1

for i, p in enumerate(problems):
    print(f"Student {i + 1} has problems {p}")
