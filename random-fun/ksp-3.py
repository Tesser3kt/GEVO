with open("file-3.in", "r", encoding="utf-8") as fin:
    N, D = tuple(map(int, fin.readline().split()))
    columns = list(map(int, fin.readline().split()))

min_height = columns[D - 1] + 1
start = D - 1
for i in range(D, N):
    if columns[i] >= min_height:
        start = i

water_units = 0
for i in range(start - 1, -1, -1):
    if columns[i] <= min_height:
        water_units += min_height - columns[i]
    else:
        min_height = columns[i]

with open("file-3.out", "w", encoding="utf-8") as fout:
    fout.write(str(water_units))
