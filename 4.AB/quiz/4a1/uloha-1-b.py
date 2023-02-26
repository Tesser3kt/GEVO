cesty = [
    [35, 10, 15],
    [10, 5, 5, 10],
    [120]
]

nejkratsi_cesta = cesty[0]
for i in range(len(cesty)):
    if len(cesty[i]) <= 3:
        if sum(cesty[i]) < sum(nejkratsi_cesta):
            nejkratsi_cesta = cesty[i]

print(sum(nejkratsi_cesta))
