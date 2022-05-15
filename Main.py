from tools.Parsers import *
from tools.Preprocessing import *
from tools.Visualization import *

TEST_DATA_AMD = "data/test/AMD.csv"
TEST_DATA_INTC = "data/test/INTC.csv"

def test_ScatterPlot():
    data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
    look_ahead = 20
    labels = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)
    test = ScatterPlot(data[0:len(data) - look_ahead], labels, show = True)

def test_ComparePlot():
    data = CSVParser(TEST_DATA_INTC).getColumnAsFloats("Close")
    look_ahead = 20
    labels1 = FixedTimeHorizonMinimized(data).label(look_ahead, 1.10, 0.90)

    sma = SimpleMovingAverage(data).label()
    labels2 = sma[0]
    data2 = sma[1]

    test = ComparePlot(data[0:len(data) - look_ahead], data2, labels1, show = True)

test_ScatterPlot()
test_ComparePlot()