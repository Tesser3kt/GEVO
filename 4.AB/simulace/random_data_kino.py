import numpy as np
import csv

HOUR_TO_TIMESTAMP = [
    None,
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
    "21:00",
]

TIMESTAMP_TO_HOUR = {
    "10:00": 1,
    "11:00": 2,
    "12:00": 3,
    "13:00": 4,
    "14:00": 5,
    "15:00": 6,
    "16:00": 7,
    "17:00": 8,
    "18:00": 9,
    "19:00": 10,
    "20:00": 11,
    "21:00": 12,
}

# Generate random data
np.random.seed(0)
data_file = open("random_data.csv", "w+", encoding="utf-8")
writer = csv.writer(data_file, delimiter=";")
writer.writerow(["Den", "Hodina", "Počet lidí"])

random_data = np.zeros((30, 12))
for day in range(1, 31):
    for hour in range(1, 13):
        if day % 7 in [0, 6]:
            if hour <= 3 or hour >= 11:
                random_data[day - 1][hour - 1] = np.random.randint(30, 70)
            if hour in range(4, 9):
                random_data[day - 1][hour - 1] = np.random.randint(100, 200)
            if hour in range(9, 11):
                random_data[day - 1][hour - 1] = np.random.randint(150, 300)
        else:
            if hour <= 3 or hour >= 11:
                random_data[day - 1][hour - 1] = np.random.randint(10, 40)
            if hour in range(4, 9):
                random_data[day - 1][hour - 1] = np.random.randint(70, 150)
            if hour in range(9, 11):
                random_data[day - 1][hour - 1] = np.random.randint(120, 250)

for day in range(1, 31):
    for hour in range(1, 13):
        writer.writerow(
            [day, HOUR_TO_TIMESTAMP[hour], int(random_data[day - 1][hour - 1])]
        )

data_file.close()
