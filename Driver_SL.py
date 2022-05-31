from tools.Parsers import *
from tools.Preprocessing import *
from tools.Instancizer import *
from tools.Runway import *
from tools.Thunderdome import *
from models.supervised.Perceptron import *
from models.supervised.KNearestNeighbor import *
from models.supervised.KNNConfidence import *

# Constants
TRAINING_FILE = "data/dev/training/INTC_2.csv"
TEST_FILE = "data/dev/testing/INTC_2.csv"
LOOK_AHEAD = 10
BUY_THRESHHOLD = 1.05
SELL_THRESHHOLD = 0.97

# Load data
parser = CSVParser(TRAINING_FILE)
close = parser.getColumnAsFloats("Close")

# Make data
mul = 2 / (LOOK_AHEAD + 1)
ema = ExponentialMovingAverage(close, mul).label()
sma = SimpleMovingAverage(close).label()

# Make labels
labels = FixedTimeHorizonMinimized(close).label(LOOK_AHEAD, BUY_THRESHHOLD, SELL_THRESHHOLD)
labels = labels[0:len(close) - LOOK_AHEAD]

def binary(data: list, label: int) -> list:
    b = []
    
    for i in range(0, len(data)):
        if data[i] == label:
            b.append(1)
        else:
            b.append(-1)
    
    return b

buy_label = binary(labels, 1)
sell_label = binary(labels, -1)

# Create instances
instances = Instancizer([close, ema[1], sma[1]], labels)
buy_instances = Instancizer([close, ema[1], sma[1]], buy_label)
sell_instances = Instancizer([close, ema[1], sma[1]], sell_label)


# Train model
NUMBER_OF_WEIGHTS = 4
LEARNING_RATE = 0.1

buy_ptron = Perceptron(buy_instances, NUMBER_OF_WEIGHTS, LEARNING_RATE)
sell_ptron = Perceptron(sell_instances, NUMBER_OF_WEIGHTS, LEARNING_RATE)

ITERATIONS = 10000
buy_ptron.computeWeights(ITERATIONS)
sell_ptron.computeWeights(ITERATIONS)

knn = KNNConfidence(instances, 5)

# Make test data
parser = CSVParser(TEST_FILE)
test_close = parser.getColumnAsFloats("Close")
test_ema = ExponentialMovingAverage(test_close, mul).label()
test_sma = SimpleMovingAverage(test_close).label()

test_instances = Instancizer([test_close, test_ema[1], test_sma[1]], labels[0:len(test_close) - LOOK_AHEAD])

"""
# Test KNNc

f = open("NeighborTests.txt", "w")
for i in range(1, 21):
    f.write(f"Using {i} neighbors\n")
    knn = KNNConfidence(instances, i)
    test = Runway(knn, test_instances, test_close, 10, False)
    f.write("---\n")
    f.write(f"Profit: ${test}\n\n")
f.close()
"""

# Test ptron
test = Thunderdome(buy_ptron, sell_ptron, test_instances, test_close, 10, False)
print(test)

# (-1299.9900119999998, 24, 0) after 1000 iterations
# (-2710.700003000001, 51, 0) after 10k iterations