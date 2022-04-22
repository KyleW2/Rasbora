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
            if self.data[i + look_ahead] / self.data[i] >= buy_threshold:
                labeled[i] = 1
            elif self.data[i + look_ahead] / self.data[i] <= sell_threshold:
                labeled[i] = -1
            else:
                labeled[i] = 0
        
        # Write to csv is save_as
        if save_as:
            f = open(save_as, "w")
            f.write("instance,label\n")
            for i in range(0, len(labeled)):
                f.write(f"{self.data[i]},{labeled[i]}\n")
        
        return labeled

class FixedTimeHorizonMinimized:
    def __init__(self, data: str) -> None:
        self.data = data
    
    def getIndexOfSmallest(self, l: list) -> int:
        smallest = 0
        for i in range(0, len(l)):
            if l[i] < l[smallest]:
                smallest = i
        
        return smallest
    
    def getIndexOfLargest(self, l: list) -> int:
        largest = 0
        for i in range(0, len(l)):
            if l[i] > l[largest]:
                largest = i
        
        return largest
    
    # TODO: gotta be a better way to do this
    def minimized(self, labeled: list) -> list:
        minimized = [0 for i in range(0, len(labeled))]

        temp = []
        index = [0]
        for i in range(0, len(labeled)-1):
            if labeled[i] == labeled[i+1]:
                temp.append(self.data[i])
                index.append(i)
            else:
                if labeled[i-1] == 1:
                    minimized[index[self.getIndexOfSmallest(temp)]] = 1
                elif labeled[i-1] == -1:
                    minimized[index[self.getIndexOfLargest(temp)]] = -1
                temp = []
                index = [0]
        
        return minimized

    def label(self, look_ahead: int, buy_threshold: float, sell_threshold: float, save_as: str = None) -> list:
        # List to store labels
        labeled = [x for x in range(0, len(self.data) - look_ahead)]

        # Loop thru data
        for i in range(0, len(self.data) - look_ahead):
            # If threshold
            if self.data[i + look_ahead] / self.data[i] >= buy_threshold:
                labeled[i] = 1
            elif self.data[i + look_ahead] / self.data[i] <= sell_threshold:
                labeled[i] = -1
            else:
                labeled[i] = 0
        
        # Minimize buy and sell labels
        minimized = self.minimized(labeled)
        
        # Write to csv is save_as
        if save_as:
            f = open(save_as, "w")
            f.write("instance,label\n")
            for i in range(0, len(minimized)):
                f.write(f"{self.data[i]},{minimized[i]}\n")
        
        return minimized