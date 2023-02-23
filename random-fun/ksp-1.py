with open("file-1.in", "r", encoding="utf-8") as fin:
    lamps = list(fin.read().strip())

for i, lamp in enumerate(lamps):
    if lamp != "O":
        continue
    if i in (0, len(lamps) - 1):
        continue

    if lamps[i - 1] == lamps[i + 1] == "O":
        lamps[i] = "-"

with open("file-1.out", "w", encoding="utf-8") as fout:
    fout.write("".join(lamps))
