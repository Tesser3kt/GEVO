import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simpy import *

# vstupní data
data = np.empty((30, 11), dtype=int)
for day in range(30):
    for hour in range(11):
        if hour <= 5:
            data[day][hour] = int(np.random.normal(150, 40))
        elif 5 < hour <= 8:
            data[day][hour] = int(np.random.normal(300, 50))
        else:
            data[day][hour] = int(np.random.normal(50, 10))

# vizualizace dat
average_day = np.mean(data, axis=0)
idx = np.arange(11, 22, 1)
ts = pd.Series(average_day, index=idx)

plt.figure(figsize=(10, 5))
plt.xticks(idx, [f"{i}:00" for i in idx])
plt.xlabel("čas")
plt.ylabel("počet diváků")
plt.title("počet diváků v kině")

ts.plot()

# výstupní data
wait_times = []

env = Environment()

num_cashiers = 3
num_ushers = 2
num_servers = 3

cashier = Resource(env, capacity=num_cashiers)
usher = Resource(env, capacity=num_ushers)
server = Resource(env, capacity=num_servers)


def purchase_ticket(env, customer):
    yield env.timeout(max(np.random.normal(3, 1), 20 / 60))


def check_ticket(env, customer):
    yield env.timeout(max(np.random.normal(3 / 60, 1 / 60), 1 / 60))


def sell_food(env, customer):
    yield env.timeout(max(np.random.normal(5, 1), 1))


def go_to_movie(env, customer, hour):
    arrival_time = env.now

    with cashier.request() as request:
        yield request
        yield env.process(purchase_ticket(env, customer))

    with usher.request() as request:
        yield request
        yield env.process(check_ticket(env, customer))

    if np.random.choice([True] * 3 + [False]):
        with server.request() as request:
            yield request
            yield env.process(sell_food(env, customer))

    if hour >= len(wait_times):
        wait_times.append([])
    wait_times[hour].append(env.now - arrival_time)


def run_theater(env):
    customer = 0
    num_of_customers = sum(np.random.poisson(average_day[hour]) for hour in range(11))
    for _ in range(num_of_customers):
        hour = int(env.now / 60)
        env.process(go_to_movie(env, customer, hour))
        customer += 1

        yield env.timeout(np.random.exponential(60 / num_of_customers))


env.process(run_theater(env))
env.run()

print(wait_times[0])
