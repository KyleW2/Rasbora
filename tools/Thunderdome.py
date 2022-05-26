from math import *

def Thunderdome(buy_model: object, sell_model: object, test_instances: list, test_prices: list, multi: int, write: bool) -> float:
    currently_holding = 0
    spent = 0
    made = 0

    b = 0
    s = 0

    for i in range(0, len(test_instances)):
        bc = buy_model.classify(test_instances[i].points)
        sc = sell_model.classify(test_instances[i].points)

        if bc == 1 and sc == -1:
            b += 1
            spent += test_prices[i]
            currently_holding += 1

        elif bc == -1 and sc == 1:
            s += 1
            made += currently_holding * test_prices[i]
            currently_holding = 0
    
    return made - spent, b, s