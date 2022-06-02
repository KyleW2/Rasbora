from Neuron import *

class NeuralNetwork:
    def __init__(self, data: list, number_of_weights: int, learning_rate: float, input_size: int, hidden_size: int, output_size: int) -> None:
        self.data = data

        self.input_layer = []
        for i in range(0, input_size):
            self.input_layer.append(Neuron(number_of_weights, learning_rate))

        self.hidden_layer = []
        for j in range(0, hidden_size):
            self.hidden_layer.append(Neuron(input_size + 1, learning_rate))
        
        self.output_layer = []
        for k in range(0, output_size):
            self.output_layer.append(Neuron(hidden_size + 1, learning_rate))

    # Output should be in 1-hot form [b, h, s] -> [1, 0, 0]
    def classify(self, y: list) -> list:
        in_classified = []
        for i in range(0, len(self.input_layer)):
            in_classified.append(self.input_layer[i].classify(y))
        
        print(in_classified)
        
        hidden_classified = []
        for j in range(0, len(self.hidden_layer)):
            hidden_classified.append(self.hidden_layer[j].classify(in_classified))

        print(hidden_classified)
        
        output_classified = []
        for k in range(0, len(self.output_layer)):
            output_classified.append(self.output_layer[k].classify(hidden_classified))
        
        return output_classified

if __name__ == "__main__":
    nn = NeuralNetwork([], 4, 0.5, 3, 6, 3)

    print(nn.classify([3, 4, 1]))

        