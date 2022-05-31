from tools.Parsers import *
from tools.Preprocessing import *
from tools.Visualization import *

TEST_DATA_AMD = "data/test/AMD.csv"
TEST_DATA_INTC = "data/test/INTC.csv"

def run_ScatterPlot():
    data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
    look_ahead = 20
    labels = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)
    test = ScatterPlot(data[0:len(data) - look_ahead], labels, show = True)

def run_ComparePlot(look_ahead: int):
    data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
    labels1 = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)

    mul = 2 / (look_ahead + 1)
    ema = ExponentialMovingAverage(data, mul).label()
    labels2 = ema[0]
    data2 = ema[1]

    test = ComparePlot(data[0:len(data) - look_ahead], data2, labels1, save = True)

def AggregateData():
    data = CSVParser("data/test/INTC.csv").getColumnAsFloats("Close")

    gator = Aggregator()
    gator.combine(["index", "price", "sma", "ema"], [[x for x in range(len(data))], data, SimpleMovingAverage(data).label()[1], ExponentialMovingAverage(data, 0.0952).label()[1]], "data/test/aggregated/INTC_agg.csv")

run_ComparePlot(20)