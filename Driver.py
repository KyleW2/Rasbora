from tools.Parsers import *
from tools.Preprocessing import *
from tools.Instancizer import *
from tools.Runway import *
from models.Perceptron import *
from models.KNearestNeighbor import *

# Constants
TRAINING_FILE = "data/dev/training/INTC.csv"
TEST_FILE = "data/dev/testing/INTC.csv"
LOOK_AHEAD = 20
BUY_THRESHHOLD = 1.10
SELL_THRESHHOLD = 0.9

# Load data
parser = CSVParser(TRAINING_FILE)
close = parser.getColumnAsFloats("Close")

# Make data
mul = 2 / (LOOK_AHEAD + 1)
ema = ExponentialMovingAverage(close, mul).label()
sma = SimpleMovingAverage(close).label()

# Make labels
labels = FixedTimeHorizonMinimized(close).label(LOOK_AHEAD, BUY_THRESHHOLD, SELL_THRESHHOLD)

# Create instances
instances = Instancizer([close, ema[1], sma[1]], labels[0:len(close) - LOOK_AHEAD])

# Train model
ptron = Perceptron(instances, 4, 0.1)
"""ptron.computeWeights(100)"""

knn = KNearestNeighbor(instances, 1)

# Make test data
parser = CSVParser(TEST_FILE)
test_close = parser.getColumnAsFloats("Close")
test_ema = ExponentialMovingAverage(test_close, mul).label()
test_sma = SimpleMovingAverage(test_close).label()

test_instances = Instancizer([test_close, test_ema[1], test_sma[1]], labels[0:len(test_close) - LOOK_AHEAD])

# Test model
test = Runway(knn, test_instances, test_close)
print(test)