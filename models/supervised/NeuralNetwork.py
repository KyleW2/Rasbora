import random
import math
import numpy as np

class Neuron:
    def __init__(self, number_of_weights: int) -> None:
        self.weights = [random.uniform(-0.05, 0.05) for i in range(0, number_of_weights)]
        self.losses = [0 for i in range(0, number_of_weights)]
    
    def dot(self, x: list) -> float:
        return np.dot(self.weights, x)
    
    def sign(self, x: list) -> float:
        return 1 / (1 + (math.e ** (-1 * self.dot(x))))
    
    def classify(self, x: list) -> float:
        return self.sign(x)
    
    def reset(self) -> None:
        for loss in self.losses:
            loss = 0

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

        for i in range(0, len(self.hidden_layers)):
            input = self.hidden_layers[i].classify(input)
            print(input)
        
        return self.output_layer.classify(input)
    
    def reset(self) -> None:
        for layer in self.hidden_layers:
            layer.reset()
        
        output_layer.reset()
    
    def back_propagate(self, training_instances: list, iterations: float) -> None:
        for i in range(0, iterations):
            self.reset()
            for t in range(0, len(training_instances)):
                Y_t = self.classify(training_instances[t].instance)
                d_t = training_instances[t].label

                """
                Update each weight's loss
                Update each weight with n/T * loss
                """



def main():
    nn = NeuralNetwork(2, (3, 3), 6)
    print(nn.classify([1, 2]))

if __name__ == "__main__":
    main()