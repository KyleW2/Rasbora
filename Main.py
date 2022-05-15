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

def run_ComparePlot():
    data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
    look_ahead = 20
    labels1 = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)

    sma = ExponentialMovingAverage(data, 0.5).label()
    labels2 = sma[0]
    data2 = sma[1]

    test = ComparePlot(data[0:len(data) - look_ahead], data2, labels1, show = True)

def AggregateData():
    data = CSVParser("data/test/INTC.csv").getColumnAsFloats("Close")

    gator = Aggregator()
    gator.combine(["index", "price", "sma"], [[x for x in range(len(data))], data, SimpleMovingAverage(data).label()[1]], "data/test/aggregated/INTC_agg.csv")

run_ComparePlot()
AggregateData()