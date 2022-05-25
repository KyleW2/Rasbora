from tools.Parsers import *
from tools.Preprocessing import *
from tools.Instancizer import *

# Constants
DATA_FILE = "data/test/INTC.csv"
LOOK_AHEAD = 20
BUY_THRESHHOLD = 1.10
SELL_THRESHHOLD = 0.9

# Load data
parser = CSVParser(DATA_FILE)
close = parser.getColumnAsFloats("Close")

# Make data
mul = 2 / (LOOK_AHEAD + 1)
ema = ExponentialMovingAverage(close, mul).label()
sma = SimpleMovingAverage(close).label()

# Make labels
labels = FixedTimeHorizonMinimized(close).label(LOOK_AHEAD, BUY_THRESHHOLD, SELL_THRESHHOLD)

# Create instances
instances = Instancizer([close, ema[1], sma[1]], labels[0:len(close) - LOOK_AHEAD])

print(instances)
# Train model