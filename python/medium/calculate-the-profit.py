# Edabit "Calculate the Profit" Challenge
# @url https://edabit.com/challenge/YfoKQWNeYETb9PYpw
# @author Odai Athamneh
# @date 2020/11/21

def main():
    # test the profit() function
    print(profit({
        "cost_price": 32.67,
        "sell_price": 45.00,
        "inventory": 1200
    })) # Expected output: 14796
    print(profit({
        "cost_price": 225.89,
        "sell_price": 550.00,
        "inventory": 100
    })) # Expected output: 32411
    print(profit({
        "cost_price": 2.77,
        "sell_price": 7.95,
        "inventory": 8500
    })) # Expected output: 44030
    return

def profit(info):
    unit_profit = info["sell_price"] - info["cost_price"]
    total_sales = unit_profit * info["inventory"]
    formatted_output = "{:.0f}".format(total_sales) # format to remove decimal places
    return int(formatted_output) # convert from string to int

main()