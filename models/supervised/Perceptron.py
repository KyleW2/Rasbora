import random
import time
import numpy

class Perceptron:
    def __init__(self, data: list, number_of_weights: int, learning_rate: float) -> None:
        self.data = data

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
    
    def computeWeights(self, iterations: int) -> None:
        for j in range(0, iterations):
            start_time = time.time()

            # Update each weight for each instance
            for i in range(0, len(self.data)):
                # w_i <- w_i + n(t - o)x
                t = self.data[i].label
                x = numpy.insert(self.data[i].points, 0, 1)
                o = self.sign(self.np_dot(x))

                # If perceptron's prediction isn't correct update weight
                if o != t:
                    for k in range(0, len(self.weights)):
                        self.weights[k] += self.n * (t - o) * x[k]
            
            print(f">> Weight iteration {j+1} done in {time.time() - start_time} seconds")
    
    def classify(self, y: list) -> float:
        return self.sign(self.dot(numpy.insert(y, 0, 1)))
    
    def saveWeights(self, f: str) -> None:
        f = open(f, "w")

        for i in range(0, len(self.weights)):
            f.write(f"{self.weights[i]}\n")
        
        f.close()