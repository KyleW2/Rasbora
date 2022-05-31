import numpy as np
from math import *

class KNNConfidence:
    def __init__(self, data: list, k: int) -> None:
        self.data = data
        self.k = k

    # Find the distance between two vectors
    def eulideanDistance(self, l1: list, l2: list) -> float:
        sum = 0
        for i in range(0, len(l1)):
            sum += (l2[i] - l1[i]) ** 2

        return sum ** (1/2)
    
    def npDistance(self, l1: list, l2: list) -> float:
        return np.linalg.norm(l2 - l1)
    
    # Return a list of disances in ascending order
    def calculateDistances(self, p: list) -> list:
        distances = []

        for i in range(0, len(self.data)):
            # Append (array of rgb, disance between) to list
            distances.append( (self.data[i], self.npDistance(self.data[i].points, p)) )
        
        distances.sort(key = lambda x: x[1])
        return distances
    
    # Classify a vector
    def classify(self, p: list) -> float:
        distances = self.calculateDistances(p)

        sum = 0
        buys = 0
        sells = 0
        for i in range(0, self.k):
            sum += distances[i][0].label

            if distances[i][0].label == 1:
                buys += 1
            if distances[i][0].label == -1:
                sells += 1

        sum = sum / self.k
        buys = buys / self.k
        sells = sells / self.k

        if sum > 0:
            return 1, buys, sells
        if sum < 0:
            return -1, buys, sells
        return 0, buys, sells