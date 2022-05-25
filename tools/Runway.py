def Runway(model: object, test_instances: list, test_prices: list) -> float:
    # Treating every buy as purchasing one share
    # Every sell is a complete dump
    buy_amount = 1
    bought = 0
    spent = 0
    made = 0

    for i in range(0, len(test_instances)):
        c = model.classify(test_instances[i].points)

        if c == 1:
            spent += buy_amount * test_prices[i]
            bought += 1
        if c == -1:
            made += bought * test_prices[i]
            bought = 0

    return made - spent