"""
General conventions:
    classes GoLikeThis
    functions goLikeThis
    variables go_like_this

Conventions for labeling:
    buy = 1
    hold = 0
    sell = -1

Terms:
    look_ahead = number of elements ahead
    buy_threshold = percent increase required for a buy
    sell_threshold = precent decrease required for a sell
"""

class FixedTimeHorizon:
    def __init__(self, data: str) -> None:
        self.data = data

    def label(self, look_ahead: int, buy_threshold: float, sell_threshold: float, save_as: str = None) -> list:
        # List to store labels
        labeled = [x for x in range(0, len(self.data) - look_ahead)]

        # Loop thru data
        for i in range(0, len(self.data) - look_ahead):
            # If threshold
            if self.data[i] / self.data[i + look_ahead] >= buy_threshold:
                labeled[i] = 1
            elif self.data[i] / self.data[i + look_ahead] <= sell_threshold:
                labeled[i] = -1
            else:
                labeled[i] = 0
        
        # Write to csv is save_as
        if save_as:
            f = open(save_as, "w")
            f.write("instance,label\n")
            for i in range(0, len(labeled)):
                f.write(f"{self.data[i]},{labeled[i]}\n")