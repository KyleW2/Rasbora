import random
import math
import numpy

class Perceptron:
    def __init__(self, number_of_weights: int, learning_rate: float) -> None:
        # Initialize weights to random value in [-1, 1]
        self.weights = [random.uniform(-0.05, 0.05) for i in range(0, number_of_weights)]
        self.n = learning_rate
    
    def dot(self, x: list) -> float:
        return numpy.dot(self.weights, x)
    
    def sign(self, x: float) -> int:
        return 1 / (1 + (math.e ** (-1 * x)))
    
    def classify(self, y: list) -> float:
        return self.sign((self.dot(y)))
    
    def update_weights(self, delta: float, x: list) -> None:
        for i in range(0, len(x)):
            self.weights[i] += self.n * delta * x[i]

class MultilayerPerceptron:
    def __init__(self, learning_rate: float, input_size: int, hidden_layers: tuple, output_size: int) -> None:
        # Input layer simply distributes the instance with an added bias
        self.input_layer = []

        # Hidden layer classifies the input forward
        ptrons_per_layer = hidden_layers[0]
        number_of_hidden_layers = hidden_layers[1]

        # List of layers
        self.hidden_layers = []

        # Append first layer with input weights
        self.hidden_layers.append([Perceptron(input_size, learning_rate) for i in range(0, ptrons_per_layer)])

        # Append other layers
        for i in range(0, number_of_hidden_layers - 1):
            self.hidden_layers.append([Perceptron(ptrons_per_layer, learning_rate) for i in range(0, ptrons_per_layer)])
        
        # Output layer classifies the hidden output with an added bias
        self.output_layer = [Perceptron(ptrons_per_layer, learning_rate) for i in range(0, output_size)]
    
    def classify(self, y: list) -> None:
        # Creates input layer
        self.input_layer = []
        for i in range(0, len(y)):
            self.input_layer.append(y[i])
        
        # Classifies the first hidden layer
        hidden_classified = [[]]
        for i in range(0, len(self.hidden_layers[0])):
            hidden_classified[0].append(self.hidden_layers[0][i].classify(self.input_layer))

        # Classify subsequent layers
        for i in range(1, len(self.hidden_layers)):
            hidden_classified.append([])
            for j in range(0, len(self.hidden_layers[i])):
                hidden_classified[i].append(self.hidden_layers[i][j].classify(hidden_classified[i-1]))
        
        # Output layer makes the final classification
        output_classified = []
        for i in range(0, len(self.output_layer)):
            output_classified.append(self.output_layer[i].classify(hidden_classified[len(hidden_classified)-1]))
        
        return output_classified
    
    def classify_by_layer(self, y: list) -> None:
        # Creates input layer
        self.input_layer = []
        for i in range(0, len(y)):
            self.input_layer.append(y[i])
        
        # Classifies the first hidden layer
        hidden_classified = [[]]
        for i in range(0, len(self.hidden_layers[0])):
            hidden_classified[0].append(self.hidden_layers[0][i].classify(self.input_layer))

        # Classify subsequent layers
        for i in range(1, len(self.hidden_layers)):
            hidden_classified.append([])
            for j in range(0, len(self.hidden_layers[i])):
                hidden_classified[i].append(self.hidden_layers[i][j].classify(hidden_classified[i-1]))
        
        # Output layer makes the final classification
        output_classified = []
        for i in range(0, len(self.output_layer)):
            output_classified.append(self.output_layer[i].classify(hidden_classified[len(hidden_classified)-1]))
        
        return self.input_layer, hidden_classified, output_classified
    
    def back_propagate(self, instances: list, iterations) -> None:
        for j in range(0, iterations):
            for i in range(0, len(instances)):
                # Get each layers feed forward classifications
                input_layer, hidden_classified, output_classified = self.classify_by_layer(instances[i].points)

                # Start computing errors backwards
                output_delta = []
                for k in range(0, len(self.output_layer)):
                    o_k = output_classified[k]
                    t_k = instances[i].label[k]
                    
                    # Compute delta
                    delta_k = o_k * (1 - o_k) * (t_k - o_k)

                    # Update output layer o_k weights
                    self.output_layer[k].update_weights(delta_k, hidden_classified)

                    # Add to list for future summations
                    output_delta.append(delta_k)
                
                # Compute errors for hidden layer
                for k in range(0, len(self.hidden_layer)):
                    o_h = hidden_classified[k]
                    t_k = instances[i].label

                    summation = 0
                    for l in range(0, len(self.hidden_layer[k].weights)):
                        summation += self.hidden_layer[k].weights[l] * output_delta[l]

                    # Compute delta
                    delta_h = o_h * (1 - o_h) * summation

                    # Update hidden layer o_h weights
                    self.hidden_layer[k].update_weights(delta_h, input_layer)

if __name__ == "__main__":
    mlp = MultilayerPerceptron(0.05, 2, (5, 1), 1)

    print(mlp.classify_by_layer([1,2]))