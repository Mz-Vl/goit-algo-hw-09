import timeit


def find_coins_greedy(amount):
    coin_values = [50, 25, 10, 5, 2, 1]
    coins_used = {}

    for coin in coin_values:
        if amount >= coin:
            coins_used[coin] = amount // coin
            amount -= coins_used[coin] * coin

    return coins_used


def find_min_coins(amount):
    coin_values = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coins_used = {}

    for i in range(1, amount + 1):
        for coin in coin_values:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coins_used[i] = coin

    coins_count = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coins_used[remaining_amount]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        remaining_amount -= coin

    return coins_count


time_greedy = timeit.timeit("find_coins_greedy(1500)", setup="from __main__ import find_coins_greedy", number=1500)

time_dp = timeit.timeit("find_min_coins(1500)", setup="from __main__ import find_min_coins", number=1500)

print("Time for the greedy algorithm:", time_greedy)
print("Dynamic programming algorithm time:", time_dp)
