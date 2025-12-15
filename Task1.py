# Реалізація жадібного алгоритму


def find_coins_greedy(amount, coins=None):
    coins = coins or [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount, coins=None):
    coins = coins or [50, 25, 10, 5, 2, 1]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


print(find_coins_greedy(113))
print(find_min_coins(113))

# {50: 2, 10: 1, 2: 1, 1: 1}
# {1: 1, 2: 1, 10: 1, 50: 2}
