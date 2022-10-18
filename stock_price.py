import math

def get_max_profit(stock_prices):
    lowest_so_far = [math.inf] # not including the current price
    max_profit = -math.inf

    for index, price in enumerate(stock_prices[1:]):
        lowest = min(lowest_so_far[index], stock_prices[index])
        lowest_so_far.append(lowest)
        max_profit = max(max_profit, price - lowest)

    if max_profit == -math.inf:
        raise Exception("Stock Prices input must have at least two elements")

    return max_profit







if __name__ == "__main__":
    print(get_max_profit(stock_prices=[]))