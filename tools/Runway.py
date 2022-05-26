from math import *

def Runway(model: object, test_instances: list, test_prices: list, multi: int, write: bool) -> float:
    # Treating every buy as purchasing one share
    # Every sell is a complete dump
    currently_holding = 0
    spent = 0
    made = 0

    b = 0
    s = 0

    if write:
        f = open("History.txt", "w")
    
    for i in range(0, len(test_instances)):
        c, buy_conf, sell_conf = model.classify(test_instances[i].points)

        if c == 1:
            spent += ceil(multi * (1 * buy_conf)) + test_prices[i]
            currently_holding += ceil(multi * (1 * buy_conf))
            b += 1

            if write:
                f.write(f"Bought {ceil(multi * (1 *buy_conf))} shares at {test_prices[i]}, currently holding {currently_holding}\n")

        if c == -1:
            made += currently_holding * test_prices[i]

            if write:
                f.write(f"Sold {currently_holding} shares at {test_prices[i]}, made {currently_holding * test_prices[i]}\n")

            currently_holding = 0
            s += 1
            

    print(f"Buys: {b}")
    print(f"Sells: {s}")

    if write:
        f.close()

    return made - spent