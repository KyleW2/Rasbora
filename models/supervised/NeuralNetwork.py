import random
import math
import numpy as np

class Neuron:
    def __init__(self, number_of_weights: int) -> None:
        self.weights = [random.uniform(-0.05, 0.05) for i in range(0, number_of_weights)]
        self.losses = [0 for i in range(0, number_of_weights)]
    
    def dot(self, x: list) -> float:
        weights_plus_bias = [w for w in self.weights]
        weights_plus_bias.insert(0, 1)
        x_plus_bias = [a for a in x]
        x_plus_bias.insert(0, 1)

        return np.dot(weights_plus_bias, x_plus_bias)
    
    def step(self, x: list) -> int:
        if self.dot(x) >= 0:
            return 1
        return 0
    
    def sigmoid(self, x: list) -> float:
        return 1 / (1 + (math.e ** (-1 * self.dot(x))))
    
    def classify(self, x: list) -> float:
        return self.step(x)
    
    def reset(self) -> None:
        for loss in self.losses:
            loss = 0
    
    def update_weights(self, n: float, T: int, loss: float, points: list) -> None:
        for i in range(0, len(self.weights)):
            self.weights[i] -= (n / T) * (loss * (-1 * points[i]))

class Layer:
    def __init__(self, number_of_neurons: int, number_of_weights: int) -> None:
        self.neurons = [Neuron(number_of_weights) for i in range(0, number_of_neurons)]
    
    def classify(self, x: list) -> list:
        output = []
        for neuron in self.neurons:
            output.append(neuron.classify(x))
        return output
    
    def reset(self) -> None:
        for neuron in self.neurons:
            neuron.reset()
    
    def update_neurons(self, n: float, T: int, loss: float, points: list) -> None:
        for neuron in self.neurons:
            neuron.update_weights(n, T, loss, points)
    
class NeuralNetwork:
    def __init__(self, learning_rate: float, input_dimension: int, hidden_dimensions: tuple, output_dimension: int) -> None:
        self.n = learning_rate
        # Create square network
        self.hidden_layers = [Layer(hidden_dimensions[1], hidden_dimensions[1]) for i in range(0, hidden_dimensions[0])]
        # Insert first hidden layer with correct number of weights
        self.hidden_layers.insert(0, Layer(hidden_dimensions[1], input_dimension))
        # Create output layer
        self.output_layer = Layer(output_dimension, hidden_dimensions[1])
    
    def classify(self, x: list) -> list:
        input = x
        output = []

        for layer in self.hidden_layers:
            input = layer.classify(input)
        
        return self.output_layer.classify(input)
    
    def reset(self) -> None:
        for layer in self.hidden_layers:
            layer.reset()
        
        self.output_layer.reset()
    
    def back_propagate(self, training_instances: list, iterations: float) -> None:
        for i in range(0, iterations):
            self.reset()
            for t in range(0, len(training_instances)):
                Y_t = self.classify(training_instances[t].points)
                d_t = training_instances[t].label

                """
                Update each weight's loss
                Update each weight with n/T * loss
                """

                # First compute d_t - Y_t to be used in all updates
                loss = np.subtract(d_t, Y_t)[0] # <- take the first index since numpy will return an array of len 1
                T = len(training_instances)

                # Pass error to all neurons for weight updates
                input = training_instances[t].points
                for layer in self.hidden_layers:
                    layer.update_neurons(self.n, T, loss, input)
                    input = layer.classify(input)
                
                self.output_layer.update_neurons(self.n, T, loss, input)


class Instance:
    def __init__(self, points: list, label: int) -> None:
        self.points = points
        self.label = label

def main():
    nn = NeuralNetwork(0.05, 2, (1, 2), 1)
    instances = [Instance([0, 0], [0]), Instance([0, 1], [1]), Instance([1, 0], [1]), Instance([1, 1], [0])]

    nn.back_propagate(instances, 1000)

    correct = 0
    for instance in instances:
        c = nn.classify(instance.points)
        
        if c == instance.label:
            correct += 1
    
    print(f"{correct} correct predictions out of {len(instances)} instances")

if __name__ == "__main__":
    main()