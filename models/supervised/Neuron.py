import random
import time
import numpy

class Neuron:
    def __init__(self, number_of_weights: int, learning_rate: float) -> None:
        # Initialize weights to random value in [-1, 1]
        self.weights = [random.uniform(-1, 1)] * number_of_weights
        self.n = learning_rate
    
    def dot(self, x: list) -> float:
        sum = 0
        for i in range(0, len(x)):
            sum += self.weights[i] * x[i]
        
        return sum
    
    def np_dot(self, x: list) -> float:
        return numpy.dot(self.weights, x)
    
    def sign(self, x: float) -> int:
        if x > 0:
            return 1
        return -1
    
    def classify(self, y: list) -> float:
        return self.sign(self.dot(numpy.insert(y, 0, 1)))
    
    def saveWeights(self, f: str) -> None:
        f = open(f, "w")

        for i in range(0, len(self.weights)):
            f.write(f"{self.weights[i]}\n")
        
        f.close()