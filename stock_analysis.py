stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65,
                53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]


def price_at(x):
    day = stock_prices[x]
    print(day)
    return day


price_at(15)


def max_price(a, b):
    day_range = stock_prices[a:b]
    maximum = max(day_range)
    print(maximum)
    return maximum


max_price(1, 20)


def min_price(a, b):
    day_range = stock_prices[a:b]
    minimum = min(day_range)
    print(minimum)
    return minimum


min_price(1, 20)
